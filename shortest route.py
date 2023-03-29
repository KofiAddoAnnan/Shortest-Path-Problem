import networkx as nx
import matplotlib.pyplot as plt
graph_net = nx.Graph()


#Add the nodes and assign the position coordinates
graph_net.add_node("Celebrity Hills Ave.", pos=(12,2))
graph_net.add_node("Lashibi", pos=(14,5))
graph_net.add_node("Sebrepor", pos=(19,7))
graph_net.add_node("Santeo", pos=(11,7))
graph_net.add_node("Teshie", pos=(7,0))
graph_net.add_node("Osu", pos=(0,0))
graph_net.add_node("Ogbodjo", pos=(5,3))
graph_net.add_node("Madina", pos=(0,6))
graph_net.add_node("Adenta Municipality", pos=(4,10))
graph_net.add_node("Gbetsile", pos=(16,11))
graph_net.add_node("Afienya", pos=(17,15))
graph_net.add_node("Bogwabo", pos=(11,20))
graph_net.add_node("Amrahia", pos=(4,20))

#Add the edges of the nodes and weight(distance in km)
graph_net.add_edge("Celebrity Hills Ave.","Lashibi",weight=10)
graph_net.add_edge("Celebrity Hills Ave.","Santeo",weight=16)
graph_net.add_edge("Celebrity Hills Ave.","Teshie",weight=9.7)
graph_net.add_edge("Celebrity Hills Ave.","Ogbodjo",weight=23)
graph_net.add_edge("Celebrity Hills Ave.","Osu",weight=19)
graph_net.add_edge("Celebrity Hills Ave.","Adenta Municipality",weight=25)
graph_net.add_edge("Lashibi","Sebrepor",weight=7.2)
graph_net.add_edge("Sebrepor","Santeo",weight=12)
graph_net.add_edge("Sebrepor","Gbetsile",weight=5.7)
graph_net.add_edge("Sebrepor","Amrahia",weight=21)
graph_net.add_edge("Santeo","Adenta Municipality",weight=13)
graph_net.add_edge("Santeo","Amrahia",weight=21)
graph_net.add_edge("Teshie","Osu",weight=9.2)
graph_net.add_edge("Osu","Ogbodjo",weight=18)
graph_net.add_edge("Osu","Madina",weight=18)
graph_net.add_edge("Ogbodjo","Madina",weight=4)
graph_net.add_edge("Ogbodjo","Adenta Municipality",weight=7.8)
graph_net.add_edge("Madina","Adenta Municipality",weight=7.8)
graph_net.add_edge("Adenta Municipality","Amrahia",weight=8.2)
graph_net.add_edge("Gbetsile","Afienya",weight=14)
graph_net.add_edge("Gbetsile","Amrahia",weight=16)
graph_net.add_edge("Afienya","Bogwabo",weight=8)
graph_net.add_edge("Afienya","Amrahia",weight=22)
graph_net.add_edge("Bogwabo","Amrahia",weight=22)


pos = nx.get_node_attributes(graph_net,'pos')
labels = nx.get_edge_attributes(graph_net,'weight')
labels = {p:f"{n} km" for p,n in labels.items()}



nx.draw(graph_net, pos, with_labels=True, font_weight= 'bold')
nx.draw_networkx_edge_labels(graph_net,pos, edge_labels= labels)


#Display the shortest path from the starting node to destination node
print('Nodes and Assigned Towns\n Node 1 = Celebrity Hills Avenue\n Node 2 = Lashibi\n Node 3 = Sebrepor\n Node 4 = Santeo\n Node 5 = Teshie\n Node 6 = Osu\n Node 7 = Ogbodjo\n Node 8 = Madina\n Node 9 = Adenta Municipality\n Node 10 = Gbetsile\n Node 11 = Afienya\n Node 12 = Bogwabo \n Node 13 = Amrahia')
print('The shortest path from Celebrity Hills Avenue (Node 1) is:- \n ', (nx.single_source_shortest_path(graph_net,source="Celebrity Hills Ave.")))

#Show graph
plt.show()
