import json
import os
import hashlib

blockchain_dir = "Blockchain_Python_lang/blockchain_form3/blockchain/"

# function เพื่อคำนวณค่า hash ของ block
def get_hash(prev_block):
    with open(blockchain_dir+prev_block,'rb')as f: # เปิดไฟล์ของ previous block
        content = f.read()                         # อ่านไฟล์แล้วเก็บเป็นชื่อว่า content
    return hashlib.sha256(content).hexdigest()     # ทำการ hash content นั้น

# function เพื่อตรวจสอบความถูกต้องของ block
def check_integrity():
    files = sorted(os.listdir(blockchain_dir),key=lambda x: int(x)) # file ทั้งหมด
    
    results = []
    
    for file in files[1:]: # วนลูปตั้งแต่ file แรกจนถึง file สุดท้าย
        with open(blockchain_dir + file) as f: # ไล่เปิดไฟล์เริ่มตั้งแต่ file แรก
            block = json.load(f)               # ให้ block เป็นตัว json ของไฟล์นั้น
        
        prev_hash = block.get("prev_block").get("hash") # get ค่า hash จาก previous block
        prev_filename =  block.get("prev_block").get("filename") # get ค่า filename จาก previous block
        
        actual_hash = get_hash(prev_filename) # หา hash ของ previous file
        
        if prev_hash == actual_hash: 
            res = "Ok"
        else:
            res = "was Changed"
        
        print(f"Block {prev_filename}:{res}")
        results.append({'block':prev_filename,'result':res})
    return results

# function การเขียน block เพิ่มลงไป           
def write_block(borrower,lender,amount):
    
    blocks_count = len(os.listdir(blockchain_dir)) # นับจำนวน block ก่อนหน้า (ตอนนี้ที่มี)
    prev_block = str(blocks_count) # ให้ previous block เป็น string จำนวนของ block ก่อนหน้า
    data = {                       # กำหนดให้ data ใน block มีอะไรบ้าง
        "borrower": borrower, 
        "lender": lender,
        "amount": amount,
        "prev_block":{
        "hash":get_hash(prev_block),
        "filename": prev_block
        }
    }
    
    current_block = blockchain_dir + str(blocks_count+1) # กำหนดให้ชื่อ current block เป็นชื่อ block เดิม +1
    
    with open(current_block,"w") as f:      # เขียนไฟล์ current block ด้วย data
        json.dump(data, f,indent=4,ensure_ascii=False)
        f.write("\n")

def main():
    #write_block(borrower="Andrew",lender="Kate",amount=100) # เพิ่มข้อมูลลง block
    check_integrity() # เช็ค block

if __name__ == '__main__':
    main()