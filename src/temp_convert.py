def far_to_kel(temp):
	return ((temp-32)/(5.0/9)) + 273.15

def kel_to_cel(temp):
	return temp - 273.15

def far_to_cel(temp):
	temp_k = far_to_kel(temp)
	result = kel_to_cel(temp_k)
	return(result)
