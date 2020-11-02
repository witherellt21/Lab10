from abstractCollection import AbstractCollection

class AbstractHeap(AbstractCollection):
   """An abstract approach to __str__ for binary tree shapes"""
   def __init__(self, sourceCollection):
      super().__init__(sourceCollection)

   def _getRoot(self):
      """Should return the way to access the root based on an implementation."""
      '''
      curPos = len(self) - 1

      while curPos > 0:
         parent = (curPos - 1) // 2
         parentItem = self._heap[parent]
         if parentItem <= item:
            break
      '''
      return 0
      #raise NotImplementedError("Abstract class method invoked.")

   def _getParent(self, index):
      """Returns access to the parent from the index or node."""
      return index // 2

   def _getLeftChild(self, index):
      """Returns access to the left child from the index or node."""
      return 2 * index

   def _getRightChild(self, index):
      """Returns access to the right child from the index or node."""
      return (2 * index) + 1

   def _getData(self, index):
      """Returns the data from the index or node."""
      return self._heap[index]

   def _insideTree(self, node):
        """Returns True if the index or node is within the tree."""
        if node != None:
            return node < len(self)

   def add(self, item):
      """To be implemented in an implementation."""
      raise NotImplementedError("Abstract class method invoked.")

   def pop(self):
      """To be implemented in an implementation."""
      raise NotImplementedError("Abstract class method invoked.")


   def __str__(self):
      """Returns a string representation with the tree rotated
         90 degrees counterclockwise."""
      def recurse(index, level):
         s = ""
         if self._insideTree(index):
            #print('hi')
            s += recurse(self._getRightChild(index), level + 1)
            s += "| " * level
            s += str(self._getData(index)) + "\n"
            s += recurse(self._getLeftChild(index), level + 1)
         return s
      return recurse(self._getRoot(), 0)
