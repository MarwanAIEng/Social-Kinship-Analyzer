
<img width="1190" height="933" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/e98a44e8-d74a-4085-84e6-370a2542ffe5" />
# Social Kinship Analyzer 🧬🤖

This is a hands-on Python project built with Pygame that turns raw social data into an interactive visual graph. Instead of looking at sterile text outputs, this tool lets you visualize how different search algorithms navigate through people's connections and friendships in real time.

The project is structured with clean, modular code to clearly demonstrate the practical differences between **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** using mouse clicks.

## ✨ Core Features
* **Full Mouse Interaction:** No clunky keyboard commands. Just click the on-screen buttons to trigger the pathfinding.
* **Smart UI Feedback:** The active button changes color immediately so you always know which algorithm is currently drawing the path.
* **Dynamic Node Coloring:** People who are part of the discovered connection path light up in bright orange, making the final route instantly clear.
* **Defensive Coding:** Uses robust data fetching to prevent the app from crashing even if a person in the network has zero connections.

## 🧠 The Algorithms Explained Simply
1. **BFS Mode (Button [B]):** This behaves like the "Mutual Friends" or "People You May Know" feature on Facebook. It scans your immediate circle first, ensuring that it always discovers the **shortest possible path** (lowest degrees of separation) between you and the target.
2. **DFS Mode (Button [F]):** This takes a deep dive. It picks one friend and follows their connection chain as deep as it goes before ever looking back. It doesn't guarantee the shortest route, but it’s perfect for exploring long, extended social chains.
<img width="1190" height="933" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/5c1dc105-f031-487d-bb94-6a2c7ad1b013" />
## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.11
* **UI/Graphics:** Pygame
* **Data Structure:** Adjacency List (Dictionary-based representation for optimized memory layout)

## 💻 How to Run it
1. Make sure you have Pygame installed:
   ```bash
   pip install pygame
