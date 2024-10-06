def process_students(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
           
            parts = line.strip().split('\t')
            if len(parts) < 4:
                continue  

            first_name = parts[0].capitalize()  
            last_name = parts[1].capitalize()   
            email = parts[2]                    
            phone = parts[3]                    

           
            if phone.startswith("555-"):
                phone_with_area_code = f"301-{phone[4:]}"
            else:
                phone_with_area_code = phone  

          
            outfile.write(f"{first_name}\t{last_name}\t{email}\t{phone_with_area_code}\n")


input_file = 'students.txt'
output_file = 'students2.txt'

process_students(input_file, output_file)

print("Processing complete. Check students2.txt for results.")
