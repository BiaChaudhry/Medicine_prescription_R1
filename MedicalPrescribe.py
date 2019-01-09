# Python Code


def main():
	print("\t{##### WELCOME TO MEDICAL PRESCRIPTION SYSTEM UNDER PYTHON #####}\t\n \t *-*-* WE HOPE THAT YOU WILL GET WELL SOON BY USING OUR SYSTEM *-*-* ")
	#printing the symptoms a system would handle
	print(" 0-headache \n 1-sore throat \n 2-chest pain \n 3-back pain \n 4-cough \n 5-pain in throat\n 6-Fatigue \n 7-Muscle aches \n 8-shortness of breath \n 9-cold sweat \n 10-nausea \n 11-lightheadedness \n 12-coughing up blood \n 13-difficulty breathing \n 14-chronic cough")
	
	#symptoms names
	symptoms = ['headache','sore throat','chest pain','back pain','cough','pain in throat','Fatigue','Muscle aches', 'shortness of breath',' cold sweat',' nausea ','lightheadedness','coughing up blood', 'difficulty breathing', 'chronic cough']

	 #illnesses relatedd to the symptoms
	illnesses = ['Meningitis','brain Tumors','Stress','Fever','Allergy','Throat Cancer(rare chance)','GERD','Artherosclerosis','Diabetes','Heart Disease','High BP','Disorders of Aorta','Tumors in chest','Poor Posture(Twisting, Bending)','Spin Inflamation']

	#medicines list for illnesses
	Medicines = ['temozolomide','Disprinenti0.1','Coricidin HBP Oral','Plavix Oral','Zostrix Topical',
	'Benzonatate Oral','Brofin','Avil','Cetuximab (Erbitux)','Syncose']

	#taking input by user for symptom on specific number as printed above
	symptomNumber = (input("Please Enter the symptom Numbers or number you want to search:")).split()
	illnessesList = []
	print('Symptoms you have entered:')

	#loop for more than 1 symptom
	for i in range(len(list(symptomNumber))):
		print(symptoms[int(symptomNumber[i])])
		illnessesPossible = (illnesses[int(symptomNumber[i])])
		illnessesList.append(illnessesPossible)
	
	#if a person has more than 1 illness than asking certain question in order to pin point the particular illness
	if len(illnessesList) > 1:
		print("well, you might be suffering from ",illnessesList)
		question01 = input("\nFrom how many days you feel like that:")
		question02 = input("\nAre you taking some other Medicine if yes then please enter the medicine name:") 
		question03 = int(input("\nPlease Enter the number of illness you feel the most from the list starting from 0 to onwards:"))
		if question03 > (len(illnessesList)-1):
			print(" Please enter the number within list ")
			question03 = int(input("Please Enter the number of illness you feel the most from the list starting from 0 to onwards:"))


		for i in range(len(list(illnessesList))):			
			print("Dear patient as you are ill and feeling this illness from ", question01 ," days \n and taking ",question02,"medicine already so,")
			print("possible illness: \n ", illnessesList[question03])
			print("Medicine: \n ", Medicines[question03])
			print("Thanks for visiting us")
			break
	else:
		#loop run if a person has only one illness
		for i in range(len(list(illnessesList))):
			print("Dear patient you are suffering from \n ",illnessesList)
			if illnessesList[i] == "brain Tumors":        
				print("medicine:",Medicines[0])
			elif illnessesList[i] == "Stress":
				print("medicine:",Medicines[3])
			elif illnessesList[i] == "cough":
				print("medicine:",Medicines[7])
			elif illnessesList[i] == "Fever":
				print("medicine:",Medicines[6])
			elif illnessesList[i] == "Throat Cancer(rare chance)":
				print("medicine:",Medicines[8])
			elif illnessesList[i] == "Allergy":
				print("medicine:",Medicines[5])
			elif illnessesList[i] == "GERD":
				print("medicine:",Medicines[3])
			elif illnessesList[i] == "Artherosclerosis":
				print("medicine:",Medicines[4])
			elif illnessesList[i] == " Diabetes":
				print("medicine:",Medicines[2])
			elif illnessesList[i] == "Heart Disease" or illnessesList[i] == "High BP" or illnessesList[i] == "Disorders of Aorta" :
				print("medicine:",Medicines[3])
			elif illnessesList[i] == "Tumors in chest":
				print("medicine:",Medicines[2])
			elif illnessesList[i] == "Poor Posture(Twisting, Bending)":
				print("medicine:",Medicines[5])
			elif illnessesList[i] == "Spin Inflamation":
				print("medicine:",Medicines[4])
main()
			
