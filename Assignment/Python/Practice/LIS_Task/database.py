import os

os.chdir("C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task1\\")


# ASTM Protocol
def au_480(file_path):
    
    MACHINE_NAME = 'AU_480'
    result = []
    
    with open(file_path, 'r') as f:
        data = f.read()

    astm_symbols = ['\x02',  '\x03',  '\x04',  '\x05',  '\x06',  '\x15',  '\x17']

    for sym in astm_symbols:
        data = data.replace(sym, '')
    # print("\n->Data: ", type(data), " \n", data)
    
      
    data_blocks = data.strip().split('D ')
    # print("\n->Data Blocks: ", type(data_blocks), " \n", data_blocks)

    for block in data_blocks:
        lines = block.strip().split()
        # print("\n->Lines: ", type(lines), "\n", lines)
        
        if len(lines) < 3:
            # print("\n->Skipping invalid block: ", type(data_blocks), " \n", lines)
            continue

        patient_id = lines[2]
        # print("\n->Patient ID:", patient_id)
        
        patient_dict = {patient_id : {}}
        
        for i in range(4, len(lines), 2):
            key = lines[i]
            val = lines[i+1]
            
            patient_dict[patient_id][key] = val
        
        # print("\n-> patient_dict: ", patient_dict)
        
        for id, tests in patient_dict.items():
            tup = (MACHINE_NAME, id, f"{tests}")
            result.append(tup)
    return result

# au_480_path = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\au_480.txt"
# au_480_output = au_480(au_480_path)

# print("\n\n-> FINAL au_480 OUTPUT: ")
# for op in au_480_output:
#     print(op)
    
# HL7 Protocol
def bc_5150(file_path):
    MACHINE_NAME = 'BC_5150'
    result = []

    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()

    control_chars = ['\x02', '\x03', '\x04', '\x05', '\x06', '\x15', '\x17', '\x1c', '\x0b']
    for sym in control_chars:
        data = data.replace(sym, '')

    # Split into messages using MSH as the start of a new message
    data_blocks = data.strip().split('MSH')
    print(f"\nTotal messages found: {len(data_blocks)-1}")  # First split part may be empty

    for block in data_blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.split('\n')  # In case \r replaced with \n
        obx_data = []

        for line in lines:
            segments = line.strip().split('|')
          
       
    
    
    
    

bc_5150_path = "C:\\practice\\Assignment\\Python\\Practice\\LIS_Task\\task2\\bc_5150.txt"
bc_5150_output = bc_5150(bc_5150_path)

print("\n\n-> FINAL bc_5150 OUTPUT: ")
for op in bc_5150_output:
    print(op)


