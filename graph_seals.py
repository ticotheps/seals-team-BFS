"""
Welcome to Part 1 of Tico's SEALs team analogy for BFT & BFS!

(*PRELUDE*):
  -So, you're probably a Lambda School student who has just conquered a 
   really difficult sprint challenge regarding data structures and 
   algorithms. That's AWESOME! You should be PUMPED!
   
  -But, hold on there, Seinfeld! The "Graphs" portion of the curriculum 
   is NOTORIOUS for being the most difficult for students! This was 
   DEFINITELY the case for "YOURS TRULY", who had to FLEX back and repeat
   the week to get more reps on BFS & DFS! And you know what? THAT'S O-KAY!
   
  -Regardless of how your classmates might be easily conquering these 
   sprints while you're struggling to keep up, remember that you're only
   "behind" if you're comparing yourself to others! If you're putting in
   the work, "PUSHING YOURSELF" means that you're constantly doing things
   OUTSIDE of YOUR perceived abilities. This is the equivalent of putting
   275 on the bar and KNOWING that you've only EVER benched 265 
   successfully on your own before.
   
  -So, while I stayed back to do another week of "Graphs", my classmates 
   moved right on ahead without me. And you probably would have thought 
   that I would be less confident in myself, but you know what? I actually 
   became MORE confident!
   
  -I mean, sure, I got more reps and more practice with BFS and DFS, but 
   something else changed! I quit trying to compete and I started to 
   challenge myself
   to HELP.

  -Instead of competing to get ahead AND STILL falling behind, I tried 
   something different this time around. I spent time helping others 
   understand what I did NOT during that FIRST week of graphs! And guess 
   what happened? JUST when I thought I was the one doing the helping, 
   light bulbs started going off for ME! 
   
  -So, this is MY opportunity to give back to the Lambda School 
   community that produced peers who were generous enough to spend 
   countless hours helping me after class, after a 2nd attempt on a sprint
   challenge, or when I just couldn't get it and felt hopeless! I just want
   to thank a few classmates that come to mind who have REALLY helped me 
   improve my understanding when I struggled the most: Julian Moreno, Jake 
   Thomas, Brandon Gardner, Lukas Siatka, Kai Lovingfoss, Jawad Hussein, & 
   Ilya Yelly-ZAR-ov. This is not an exhaustive list by any means, but just 
   those that picked me up when I fell the hardest.
   
  -By the way, I was inspired by Nick Durbin to make this tutorial. Nick is 
   another extremely selfless student that I've met at Lambda School, who 
   you should definitely follow on Twitter and subscribe to on YouTube! The 
   guy is super motivating and so helpful! I'll drop his Twitter handle and 
   YouTube account in the description box below!
  
(*Overview*):

  -Okay. So NOW, let's get to the analogy that I came up with while helping 
   some classmates better understand Breadth First Traversal & Breadth 
   First Search during my second week with "Graphs"!
   
  -First, we need to understand the difference between BFT and BFS!
  
  -One ends with "traversal" and the other ends with "search".
  
  -What is "traversal"? Well, in the context of "graphs", it just means that 
   we want to visit every vertex in the graph, ONCE. I think a good analogy
   for this could be counting out all 52 cards, in a deck, just to make sure
   you have all 52 cards in there. No matter what game you plan on playing,
   you'll always visit EACH card, once, to make sure they're all there 
   before you play, right? (nods head)
   
  -Well, what is "search" then, Tico? When it comes to BFT & BFS, "search" 
   is very similar to "traversal" except you don't HAVE TO visit EVERY 
   vertex ONCE because you can STOP once you find the vertex you're looking
   for. So, using the "cards" analogy, you could think of someone who isn't
   very good at magic tricks doing a card trick on you where they
   continually ask you, "Is this your card?" until they've gone through
   about half of the deck before finding "your card", right? Because they
   don't have to keep saying "Is this your card?" for all the remaining
   cards that they haven't flipped over yet, right? Nope! They stop when
   they find the card they're looking for!  
   
  -Now that you know what "traversal" and "search" mean in this context,
   what does "BREADTH first" mean?
   
  -We can think of "breadth" as meaning "wide", or "broad", or 
   "all-inclusive".
   
  -So, if you look at this graph on the left, you can see that the solid
   blue arrows, which represent "searching" or movement through the graph,
   are moving in a generally DOWNWARD direction, from the top of the graph
   to the bottom of the graph, right?
   
  -BUT notice that the solid blue arrows don't move diagonally, to the 
   NEXT level, until EVERY vertex in the PREVIOUS level has been visited 
   ONCE.
   
  -So, when I think of "Breadth First SEARCH (or traversal)" I think of 
   an olympic decathlete, who is focused on making sure they are EQUALLY 
   good in 10 DIFFERENT track & field events, BEFORE they try to LEVEL UP
   in any ONE of the events.
   
  -So, if you look at each VERTEX like a "skill" or "track event", you
   can see what I mean. The decathlete on the left (or BREADTH FIRST 
   SEARCH) is more concerned that he reaches "level 2" in EACH of his 
   events, the 100-meter dash AND the 110-meter hurdles, BEFORE he tries
   to improve to "level 3" in EITHER of those events.
   
  -On the other hand, you have the olympic sprinter on the right (or DEPTH
   FIRST SEARCH), who is more concerned about reaching the HIGHEST level
   in his main event, the 100-meter dash, before trying to LEVEL UP, at 
   ALL, in another skill of his, the 110-meter hurdles. He's more of an 
   "ALL IN" or "ALL OUT kind of guy".
   
  -So now that you have a pretty good idea of what BFT and BFS are doing,
   at a high level, let's take a look at an example I created while helping
   some classmates better understand what these algorithms are doing, line
   by line.
   
  (*Scenario*):
  
  -Alright. So, let's pretend you're a Lambda School student, who ALSO 
   happens to be a part-time Navy SEAL lieutenant (LT).
  
  -You and your team of tactical problem solvers have just been deployed 
   to a foreign country on a special mission. 

  -Your objective is to recover this U.S. Ambassador that has been 
   kidnapped by a terrorist! 
   
  -OH NO! How will we know where to begin looking? Not to worry!
  
  -Remember this recent cryptic tweet from Lambda School's CEO, Austen?
   I DE-crypted it!
  
  -So check this out! Yep. Turns out Tony Stark was the recent mystery grad 
   from Lambda School and the C.I.A. just hired Tony for a whopping $110 
   million/year. My man, Austen, left out a few zeros in his tweet, either
   because he's super humble or because he must have gotten distracted, mid-
   tweet, by the Slack bot in the #hiring channel.
   
  -Anyways, Tony happens to be on the same project as your SEALS team and he 
   found the exact location where the terrorist is currently holding our
   Ambassador---in this abandoned warehouse. Dang! You gotta get me one of 
   those keyboards, Tony!
   
  -So now a stealth chopper has flown right over the target location so you
   and your team could propel down and search that 5-level abandoned warehouse
   for our Ambassador.
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    # Think of the graph as a partially-completed map of an "abandoned 
    #   warehouse" that the SEALS team must use and continually update
    #   as they search for this bad guy.
    # Due to limited intel, think of ANY vertex of the graph as a "room"
    #   inside of this "warehouse" that may OR may NOT be on our 
    #   partially-completed map.
    def __init__(self):
        # This is a set(), which is just an unordered & unindexed 
        #   collection in Python.
        # Think of this set() as the physical piece of paper that our map
        #   will be drawn on by our SEALS as they keep track of which.
        self.vertices = {}
    # Any room that does NOT have AT LEAST one edge is considered
    #   a "SECRET room".
    def add_vertex(self, vertex_id):
        # Uncovers another pre-existing "SECRET room" in the "warehouse".
        self.vertices[vertex_id] = set()
    def add_edge(self, vertex_1_id, vertex_2_id):
        # Uncovers another pre-existing "SECRET room" in the "warehouse".
        if vertex_1_id in self.vertices and vertex_2_id in self.vertices:
            self.vertices[vertex_1_id].add(vertex_2_id)
        else:
            raise IndexError("That vertex does not exist")
          
    # You are a Navy Seal and your mission is traverse through each room
    #   (AKA "search each room") in the building for a bad guy.
    def bft(self, starting_vertex_id):
        # Step 1: Create an empty QUEUE and enqueue the starting_vertex_id
        q = Queue()
        q.enqueue(starting_vertex_id)
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while queue is NOT empty
        while q.size() > 0:
            # Step 4: Dequeue the FIRST vertex [to evaluate] and set it equal
            #         to a variable
            current_vert = q.dequeue()
            if current_vert not in visited:
                # Step 5: If it has NOT been visited, print it and add it 
                #         into the set as an item
                print(current_vert)
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over each of current_vert's
                #         neighbors, adding each one to end of the queue
                for next_vert in self.vertices[current_vert]:
                    q.enqueue(next_vert)
        
    def dft(self, starting_vertex_id):
        # Step 1: Create an empty STACK and push the starting_vertex_id
        s = Stack()
        s.push(starting_vertex_id)
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while stack is NOT empty
        while s.size() > 0:
            # Step 4: Pop the FIRST vertex [to evaluate] and set it equal
            #         to a variable
            current_vert = s.pop()
            if current_vert not in visited:
                # Step 5: If it has NOT been visited, print it and add it 
                #         into the set as an item
                print(current_vert)
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over each of current_vert's
                #         neighbors, adding each one to end of the queue
                for next_vert in self.vertices[current_vert]:
                    s.push(next_vert)
                    
    def dft_recursive(self, starting_vertex_id, visited=None):
        # Step 1: Check to see if a set() to store visited vertices exists.
        #         If not, create one.
        if visited is None:
            visited = set()
        # Step 2: Check to see if starting_vertex_id is in the set(). 
        if starting_vertex_id not in visited:
            # Step 3: If not, print it and add it to the set().
            print(starting_vertex_id)
            visited.add(starting_vertex_id)
            # Step 4: Use a FOR loop that iterates over each of starting_vertex_id's
            #         neighbors, calling the dft_recursive() method on each one
            for neighbor in self.vertices[starting_vertex_id]:
                self.dft_recursive(neighbor, visited)
                
    def bfs(self, starting_vertex_id, destination_vertex_id):
        # Step 1: Create an empty QUEUE and enqueue the starting_vertex_id,
        #         WITHIN an array, to the end of the queue (b/c we're 
        #         storing PATHS this time, not "vertices")
        q = Queue()
        q.enqueue( [starting_vertex_id] )
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while queue is NOT empty
        while q.size() > 0:
            # Step 4a: Dequeue the FIRST PATH [to evaluate each of it's 
            #         vertices] and set it equal to a variable
            path = q.dequeue()
            # Step 4b: Grab the VERTEX from the end of the path [to evaluate]
            current_vert = path[-1]
            # Step 4c: If current_vert == destination_vertex_id, return path
            if current_vert == destination_vertex_id:
                return path
            if current_vert not in visited:
            # Step 5: If the current_vert has NOT been visited, add it into the 
            #         set() as an item
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over EACH of 
                #         current_vert's neighbors, creating a NEW 
                #         copy of the path for EACH neighbor, but each
                #         neighbor now becomes the NEW 'current_vert'
                #         for their OWN path, which is added to the
                #         end of the queue, to be evaluated later
                for neighbor in self.vertices[current_vert]:
                    # Step 7: Copy the path
                    path_copy = list(path)
                    # Step 8: Append the neighbor to the end of the copied path
                    path_copy.append(neighbor)
                    # Step 9: Enqueue the copied path
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex_id, destination_vertex_id):
        # Step 1: Create an empty STACK and push the starting_vertex_id,
        #         WITHIN an array, to the end of the stack (b/c we're 
        #         storing PATHS this time, not "vertices")
        s = Stack()
        s.push( [starting_vertex_id] )
        # Step 2: Create a Set() to store visited vertices
        #         NOTE: Sets are a good data structure b/c: they're 
        #               unordered and don't have duplicated items
        visited = set()
        # Step 3: Use a WHILE loop that continues while the stack is NOT empty
        while s.size() > 0:
            # Step 4a: Pop the FIRST PATH [to evaluate each of it's 
            #         vertices] and set it equal to a variable
            path = s.pop()
            # Step 4b: Grab the VERTEX from the end of the path [to evaluate]
            current_vert = path[-1]
            # Step 4c: If current_vert == destination_vertex_id, return path
            if current_vert == destination_vertex_id:
                return path
            if current_vert not in visited:
            # Step 5: If the current_vert has NOT been visited, add it into the 
            #         set() as an item
                visited.add(current_vert)
                # Step 6: Use a FOR loop that iterates over EACH of 
                #         current_vert's neighbors, creating a NEW 
                #         copy of the path for EACH neighbor, but each
                #         neighbor NOW becomes the NEW 'current_vert'
                #         for their OWN path, which is added to the
                #         end of the queue, to be evaluated later
                for neighbor in self.vertices[current_vert]:
                    # Step 7: Copy the path
                    path_copy = list(path) # Creates a copy of the list
                    # Step 8: Append the neighbor to the end of the copied path
                    path_copy.append(neighbor)
                    # Step 9: Push the copied path
                    s.push(path_copy)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Vertices in Graph:\n")
    print(graph.vertices)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("DFT path:")
    graph.dft(1)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("BFT path:")
    graph.bft(1)
    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("DFT-recursive path:")
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("BFS path with shortest # nodes:")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\n\n---------------------------------------------------------------\n")
    print("DFS path in depth first order:")
    print(graph.dfs(1, 6))
