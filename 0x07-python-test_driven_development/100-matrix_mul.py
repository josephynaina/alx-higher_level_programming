#!/usr/bin/python3

"""
module to multiply two matrices
"""
class check_matrix:

    def __init__(self, mat, mat_name):
        """
        init metho initialises the value mat name and mat value
        """

        self.__mat_name = mat_name
        self.__mat = mat
        self.check_is_list()
        self.check_is_list_of_lists()
        self.check_is_empty()
        self.check_elements()
        self.check_is_rectangle()
    
    def check_is_list(self):
        """
        raises type error if matrix is not list
        """

        message = self.__mat_name + ' must be a list'
        if type(self.__mat) is not list:
            raise TypeError(message)

    def check_is_list_of_lists(self):
        """
        raise type error if matrix is not a list of lists
        """

        message = self.__mat_name + ' must be a list of lists'
        for i in self.__mat:
            if type(i) is not list:
                raise TypeError(message)

    def check_is_empty(self):
        """
        raise valueerror if matrix has no elements
        """

        message = self.__mat_name + " can't be empty"
        if len(self.__mat) == 0:
            raise ValueError(message)
        for i in self.__mat:
            if len(i) == 0:
                raise ValueError(message)

    def check_elements(self):
        """
        raise type errror if an element of matrix is not an int or a float
        """

        message = self.__mat_name + " should contain only integers or floats"
        for i in  self.__mat:
            for j in i:
                if type(j) not in [int, float]:
                    raise TypeError(message)
    def check_is_rectangle(self):
        """
        raise type error if rows of a matrix are not equal in length
        """

        message = "each row of " + self.__mat_name + " must be of the same size"
        a = len(self.__mat[0])
        for i in self.__mat:
            if len(i) != a:
                raise TypeError(message)

def matrix_mul(m_a, m_b):

    """
    function to multiply two matrices
    """

    #checks for matrix a
    a = check_matrix(m_a, 'm_a')
    b = check_matrix(m_b, 'm_b')

    check_can_mul(m_a, m_b)

    ans = []
    ans_row = []
    ans_elem = 0
    i = 0
    j = 0
    
    while i < len(m_a):
        while j < len(m_a[i]):
            ans_elem = mul_row_column(get_row(m_a, i), get_column(m_b, j))
            ans_row.append(ans_elem)
            j += 1
        ans.append(ans_row)
        ans_row = []
        j = 0
        i += 1

    return ans

def get_row(mat, row):
    """
    exract a row from a matrix
    """

    return mat[row]

def get_column(mat, column):
    """
    extract a column from a matrix
    """

    l = len(mat)
    c = []
    i = 0
    while i < l:
        c.append(mat[i][column])
        i += 1
    return c
def mul_row_column(row, column):
    """
    multiply the elements of a row and a column
    """

    i = 0
    value = 0
    while i < len(row):
        value += row[i] * column[i]
        i += 1
    return value

def check_can_mul(m_a, m_b):
    """
    check that m_a is multipliable to m_b
    """

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
