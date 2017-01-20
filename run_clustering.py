if __name__ == '__main__':
    query = sys.argv[1]
    from knn_graph_clustering import *
    c = manager.Client()
    res = c.my_text_search(query=query)
    b = c.new_basket()
    b.load_sounds(res)
    cluster = Cluster(basket=b)
    cluster.run()