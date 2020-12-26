# Huffman Encoder Decoder

## Overview - Data Compression
In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data.
A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm.

## Huffman Logic
### A. Huffman Encoding
We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data.

#### Phase I - Build the Huffman Tree
A Huffman tree is built in a bottom-up approach.
- First, determine the frequency of each character in the message.
- Each row in the table above can be represented as a node having a character, frequency, left child, and right.
- Heap the nodes.
- Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
- Create a new node with a frequency equal to the sum of the two nodes picked in the above step. This new node would become an internal node in the Huffman tree, and the two nodes would become the children. The lower frequency node becomes a left child, and the higher frequency node becomes the right child. Reinsert the newly created node back into the priority queue.
- Repeat previous two steps until there is a single element left in the priority queue.
- For each node, in the Huffman tree, assign a bit 0 for left child and a 1 for right child.

#### Phase II - Generate the Encoded Data
- Based on the Huffman tree, generate unique binary code for each character of a string message. Traverse the path from root to the leaf node.

### B. Huffman Decoding

Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data using the following steps:
- Pick a bit from the encoded data, traversing from left to right.
- Start traversing the Huffman tree from the root.
- If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
- If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
- Repeat steps until the encoded data is completely traversed.