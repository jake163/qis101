#!/usr/bin/env python3 #shell bang allows us to run python scripts from 
#command line
# k_means.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

K_CLUSTERS = 3 #declaring three global variables, 3 clusters
INCLUDE_OUTLIERS = True #i.e. exclude outliers
MEAN_MULTIPLE = 3


class DataPoint: #object oriented design, class is a user defined data type,
    #can contain callable functions
    def __init__(self, x, y): #dunder declare constructor for
        #class
        self.x = x
        self.y = y
        self.cluster = None #cluster is a number, initially we set to None

    def __repr__(self): #returns a string, set of characters you can paste
        #into another python file to recreate the class
        return f"DataPoint({self.x}, {self.y})"


class Cluster: #
    def __init__(self, index): #cluster has an index number
        self.index = index
        self.x = 0.0 #mew point
        self.y = 0.0
        self.population = 0 #tracks # of data points in a cluster
        self.mean_distance = 0.0 #how far on average is each data point
        #from mean

        colmap = ("red", "blue", "green", "purple", "yellow", "orange")
        #each cluster has a color
        self.color = colmap[index]

    def __repr__(self):
        return f"Cluster({self.index})"


def init_clusters(k): #make a list of clusters
    clusters = [Cluster(i) for i in range(k)] #list comprehension
    return clusters


def init_points(file_name): #open csv
    samples = np.genfromtxt(f"{file_name}", delimiter=",")
    points = [] #list of data point objects
    for s in samples:
        point = DataPoint(s[0], s[1]) #pass first and second column
        #into data point constructor
        points.append(point) #add that to points
    return points


def init_assign(points, clusters): # pass in list of points and clusters
    k = len(clusters) #k is number of clusters
    for idx, p in enumerate(points):
        c = clusters[idx % k] #gives number between 0 and k - 1
        p.cluster = c #c is the cluster number
        c.population += 1


def reassign(points, clusters):
    converged = True #assume clusters are converged

    # Phase I: Calculate the new geometric mean of each
    # cluster based upon current data point assignments
    for c in clusters: #for every cluster
        new_x, new_y = 0, 0 #init new variable
        for p in points: #for every point
            if p.cluster == c: #if point cluster number is c
                new_x += p.x #add x
                new_y += p.y
        new_x /= c.population #calculate new mean x
        new_y /= c.population

        if c.x != new_x or c.y != new_y:
            c.x, c.y = new_x, new_y #update mew point if necessary
            converged = False #if we had to update, than we are not 
            #converged

    # Phase II: Assign data points to nearest cluster
    for p in points: #go through every data point
        dist_min = sys.float_info.max #which cluster has min distance
        nearest_cluster = None #don't know nearest cluster
        for c in clusters:
            dist = np.hypot(p.x - c.x, p.y - c.y) #for every cluster find
            #pythagorean distance
            if dist < dist_min:
                dist_min = dist #if we've found a shorted distance, then
                #this is the new distance
                nearest_cluster = c
        if nearest_cluster != p.cluster:
            if p.cluster.population > 1: #point can leave cluster if it 
                #isn't the only one
                p.cluster.population -= 1 #decrease pop by one
                p.cluster = nearest_cluster #set cluster number by new 
                #cluster
                p.cluster.population += 1 #new cluster has incr. by one
                converged = False #not converged

    # Phase III - Evict any point too far away from its cluster's center
    if converged and MEAN_MULTIPLE > 0:
        # Calculate mean distance from each cluster's center
        # to the assigned points for that cluster
        for c in clusters:
            total_distance = 0.0
            for p in points:
                if p.cluster == c:
                    total_distance += np.hypot(p.x - c.x, p.y - c.y)
            c.mean_distance = total_distance / c.population

        # Only keep points where the distance to its assigned cluster's
        # center is less than a multiple of that cluster's mean distance
        # to its assigned points
        new_points = []
        for p in points:
            c = p.cluster
            dist = np.hypot(p.x - c.x, p.y - c.y)
            if dist < c.mean_distance * MEAN_MULTIPLE:
                new_points.append(p)
            else:
                if c.population > 1:
                    print(f"Evicted {p} from {c}")
                    c.population -= 1
                    converged = False
        points[:] = new_points

    return converged


def plot(ax, points, clusters):
    ax.set_aspect("equal")
    ax.set_xlim(-5, 45)
    ax.set_ylim(-5, 45)
    ax.set_title(f"k-Means Clustering (k={K_CLUSTERS})") #title with repl.
    #for k_clusters

    for p in points: #every cluster has color, use that to color data point
        #alpha makes it semi transparent
        ax.scatter(p.x, p.y, color=p.cluster.color, alpha=0.5, edgecolor="black")

    for c in clusters: #draw the mew point in each cluster
        #s is for square
        ax.scatter(c.x, c.y, color=c.color, marker="s")


def on_key_press(event, ax, points, clusters):
    if event.key == "n": #if you press lowercase n
        if reassign(points, clusters): #if it has reached equilibrium
            print("Cluster has converged!")
        ax.clear()
        plot(ax, points, clusters)
        plt.draw()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])

    key_press_event = fig.canvas.mpl_connect( #interact with code execution
    #via a key press
        "key_press_event", lambda event: on_key_press(event, ax, points, clusters)
    )

    clusters = init_clusters(K_CLUSTERS) #read in data file, initialize
    #clusters

    file_name = os.path.dirname(sys.argv[0]) + "/cluster_samples.csv"
    points = init_points(file_name) #read in file and parse for points

    if not INCLUDE_OUTLIERS: #remove outliers
        points.pop()

    init_assign(points, clusters) #initial assign

    plot(ax, points, clusters) #plot points and clusters

    plt.show()


if __name__ == "__main__":
    main()
