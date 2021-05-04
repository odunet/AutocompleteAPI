# define Python user-defined exceptions
class TriesError(Exception):
    """Base class for other exceptions"""

    def __init__(self, msg='Kindly review datastructure documentation', *args, **kwargs):
        """
        """
        super().__init__(msg, *args, **kwargs)
        self.keyError = "ERROR Tries: The Key: " + \
            str(msg) + ", is not stored in the Tries!"
        self.dictError = "ERROR Tries: The Tries table is" + \
            " empty"


class Tries:
    """
    A class used to represent a Trie data structure

    ...

    Attributes
    ----------
    table : dictionary (Not user defined)
        a dictionary containing key, value pairs with entries in a tries structure
        For example, below is a dictionary sructure containing one word entry, i.e.
        "ayokunle". The preceeding keys i.e. 97 - 101 are the ASCII values of the letters.
        {'97': {'121': {'111': {'107': {'117': {'110': {'108': {'101': {'ayokunle': 'ayokunle'}}}}}
    autocomplete : bool (User defined, default = False)
        a bool value that tells the class if the Trie will be used for autocomplete. Tries used for
        autocomplete, are strict because they require the following:
        1) Key and value must equal each other and they must be strings.


    Methods
    -------
    get_dictList(dictionary = {})
            Parameters
            ----------
            dictionary : dictionary
                A dictionary object (default is
                {})


            Returns
            -------
            list
                a list of strings used that are the disctionary keys.

    raise_error(key = None)
            Parameters
            ----------
            key : str
                A dictionary key (default is
                None)


            Returns
            -------
            Exeption
                a strings showing the exeption and key involved.

    autoRecursion(dictionary = {}, result)
            Parameters
            ----------
            dictionary : dictionary
                A dictionary object (default is
                {})
           result : list
                An empty list object that takes the result

            Returns
            -------
            list
                a list of strings showing the text completion suggestion

    __setitem__(key = None, value = None)
            Parameters
            ----------
            key : N/A (Value must be string if Tries is used for autocomplete)
                A key for value stored in the Trie
            value : N/A (Value must be string if Tries is used for autocomplete)
                A value stored in the Trie

            Returns
            -------
            dictionary
                a dictionary containing key, value pairs with entries in a tries structure
                For example, below is a dictionary sructure containing one word entry, i.e.
                "ayokunle". The preceeding keys i.e. 97 - 101 are the ASCII values of the letters.
                {'97': {'121': {'111': {'107': {'117': {'110': {'108': {'101': {'ayokunle': 'ayokunle'}}}}}

    __getitem__(key = None)
            Parameters
            ----------
            key : N/A (Value must be previously string if Tries)
                A key for value stored in the Trie

            Returns
            -------
            dictionary
                a dictionary containing key, value pairs with entries in a tries structure
                For example, below is a dictionary sructure containing one word entry, i.e.
                "ayokunle". The preceeding keys i.e. 97 - 101 are the ASCII values of the letters.
                {'97': {'121': {'111': {'107': {'117': {'110': {'108': {'101': {'ayokunle': 'ayokunle'}}}}}

    autosearch(key = None)
            Parameters
            ----------
            key : N/A (Value must be previously string if Tries)
                A key for value stored in the Trie

            Returns
            -------
            tuple
                a boolean and a list. The list contains strings of predicted autocomplete items e.g.:
                (True, ['oluwatosin', 'oluwaseun', 'oluwasegun', 'oluwakemi', 'olumide', 'olufunso',
                'olufemi', 'oluremi', 'olushola'])
    """

    def __init__(self, autocomplete=False):
        self.table = {}
        if type(autocomplete) != bool:
            self.autocomplete = False
        else:
            self.autocomplete = autocomplete

    def __repr__(self):
        rep = "The Tries is: " + str(self.table)
        return rep

    def get_dictList(self, dictionary={}):
        if not dictionary:
            return False
        else:
            lst = list(dictionary.keys())
            return lst

    def raise_error(self, key=None):
        try:
            raise TriesError(str(key))
        except TriesError as e:
            if key == None:
                print(e.dictError)
            else:
                print(e.keyError)

    def autoRecursion(self, dictionary, result):
        if not dictionary:
            return
        arr = self.get_dictList(dictionary)
        counter = 0
        for k in dictionary:
            if ord(arr[counter][0]) >= 97 and ord(arr[counter][0]) <= 122:
                result.append(dictionary[k])
                self.autoRecursion({}, result)
            else:
                self.autoRecursion(dictionary[k], result)
            counter += 1

    def __setitem__(self, key=None, value=None):
        if key == None or value == None:
            return "Error Key: " + str(key) + " or Value: " + str(value) + " not acceptable."

        # # Statement below evaluates if Trie willl be used for auto-complete
        if (self.autocomplete):
            if key != value or type(key) != str:
                print("Error Key: " + str(key) + " or Value: " +
                      str(value) + " not acceptable.")
                return

        tempDictA = self.table
        counter = 0

        for index, i in enumerate(key):
            counter += 1
            tempAscii = ord(i)
            if not tempDictA:  # Trie is empty
                tempDictA.update({str(tempAscii): {}})
            elif counter == 1:  # First letter of key already in Tries
                # If first letter of key is in first level of Tries
                if str(tempAscii) in self.get_dictList(tempDictA):
                    if len(key) == 1:
                        tempDictA[str(tempAscii)].update({key: value})
                        return self.table  # Return imediately
                else:
                    if len(key) == 1:
                        tempDictA.update({str(tempAscii): {}})
                        tempDictA[str(tempAscii)].update({key: value})
                        return self.table  # Return imediately
                    else:
                        tempDictA.update({str(tempAscii): {}})
            elif counter > 1:
                tempDictB = {}
                for j in range(counter - 1):
                    if j == 0:
                        tempDictB = tempDictA[str(ord(key[j]))]
                    else:
                        tempDictB = tempDictB[str(ord(key[j]))]

                    if j == len(key) - 2:  # Evaluate if this is the last key
                        try:  # Evaluate without error if node was previoduly created
                            if tempDictB[str(tempAscii)]:
                                tempDictB[str(tempAscii)].update({key: value})
                        except:
                            tempDictB.update({str(tempAscii): {}})

                            tempDictB[str(tempAscii)].update({key: value})

                # Evaluate if this is not the last key
                if j != len(key) - 2:
                    try:  # Evaluate without error if node was previoduly created
                        if not tempDictB[str(tempAscii)]:
                            tempDictB.update({str(tempAscii): {}})
                    except:
                        tempDictB.update({str(tempAscii): {}})

        return self.table

    def __getitem__(self, key):
        if key == None:
            return "Error Key: " + str(key) + " not acceptable."
        if not self.table:
            self.raise_error()
            return

        tempDictA = self.table
        counter = 0

        for index, i in enumerate(key):
            counter += 1
            tempAscii = ord(i)
            # Evaluates if first letter of key is not in first node level
            if str(tempAscii) not in self.get_dictList(tempDictA) and counter == 1:
                self.raise_error(key)
            # Evaluates if first letter of key is in first node level
            elif counter == 1:
                if len(key) == 1:
                    return tempDictA[str(tempAscii)][key]
            # Evaluates for all nodes after the first
            else:
                tempDictB = {}
                for j in range(counter - 1):
                    if j == 0:
                        tempDictB = tempDictA[str(ord(key[j]))]
                    else:
                        tempDictB = tempDictB[str(ord(key[j]))]

                    if j == len(key) - 2:  # Evaluate if this is the last key
                        if str(tempAscii) not in self.get_dictList(tempDictB):
                            self.raise_error(key)

                        else:
                            return tempDictB[str(tempAscii)][key]

                # Evaluate if this is not the last key
                if j != len(key) - 2:
                    if str(tempAscii) not in self.get_dictList(tempDictB):
                        self.raise_error(key)

        return self.table

    def autoSearch(self, key):
        # if key == None:
        #     return
        tempDictA = self.table
        counter = 0
        autoTuple = []

        for index, i in enumerate(key):
            counter += 1
            tempAscii = ord(i)
            # Evaluates if first letter of key is not in first node level
            if str(tempAscii) not in self.get_dictList(tempDictA) and counter == 1:
                self.raise_error(key)
                return (False, [])
            # Evaluates if first letter of key is in first node level
            elif counter == 1:
                if len(key) == 1:
                    return (False, [])
            # Evaluates for all nodes after the first
            else:
                tempDictB = {}
                for j in range(counter - 1):
                    # Check that we are in first iter
                    if j == 0:
                        # If key item is not in node, and break
                        if str(ord(key[j])) not in self.get_dictList(tempDictA):
                            break
                        else:
                            tempDictB = tempDictA[str(ord(key[j]))]
                    else:
                        # If key item is not in node, and break
                        if str(ord(key[j])) not in self.get_dictList(tempDictB):
                            break
                        else:
                            tempDictB = tempDictB[str(ord(key[j]))]

                    if j == len(key) - 2:  # Evaluate if this is the last letter in key
                        # If key item is not in node, and break
                        if str(str(tempAscii)) not in self.get_dictList(tempDictB):
                            break
                        self.autoRecursion(
                            tempDictB[str(tempAscii)], autoTuple)
        if not autoTuple:
            return (False, autoTuple)
        else:
            return (True, autoTuple)


if __name__ == "__main__":
    pass
