icNssPersonnel = ["Rahma", "Nelson", "Fadl", "Antiaye", "Jensen", "Kwesi", "Philip", "Ian", "Habib", "Darien", "Kaisaan"]
print(icNssPersonnel)
poppedPersonnel = icNssPersonnel.pop() # pop removes the last element from the list, but allows you to use the value.
print(poppedPersonnel + " has been popped. The current NSS personnel are:")
print(icNssPersonnel)
personnelHead = icNssPersonnel.pop(3) # you can pop at any index if you provide it.
print(personnelHead + " has been elevated to Studio Manager. His subordinates are: ")
print(icNssPersonnel)
engineeringHead = "Habib"
icNssPersonnel.remove(engineeringHead) # use remove to remove the first occurence of an item in a list
print(engineeringHead + " is the head of engineering")
icNssPersonnel.sort() # sort the list alphabetically
print("The NSS personnel with their names sorted alphabetically are:") 
print(icNssPersonnel)
print(); print(); print(); print()
numbers = [3, 15, 1, 28028, 8520, 20570829,20590,207808, 20857,9089, 29098,54802,5982,28508,10570,50829]
print(sorted(numbers)) # sorted sorts the list, but preserves the original list
print(sorted(numbers, reverse=True))
print(); print(); print(); print()
favoriteArtists = ["Agbovi", "Asake", "Uncle Waffles", "Scotts Maphuma", "Chle", "Tulenkey", "Zlatan", "Kofi Mole", "Shallipopi", "Zerry DL", "Famous Pluto", "Smur Lee"]
favoriteArtists.reverse() # reverses the order of elements in a list without sorting them
print(favoriteArtists)
print(len(favoriteArtists)) # finds the length of a list