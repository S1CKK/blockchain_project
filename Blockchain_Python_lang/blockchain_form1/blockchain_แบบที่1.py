import datetime
import json 
import hashlib
from urllib import response
from flask import Flask, jsonify
# สร้าง genesis block

# step 1 - ออกแบบ class ของ blockchain

class Blockchain:
    # constructor
    def __init__(self):
        # เก็บกลุ่มของ block
        self.chain = [] # list ที่เก็บ block
        self.transaction = 0 # amount of money
        # genesis block
        self.create_block(nonce=1,previous_hash="0")
        
    # สร้าง block ขึ้นมาในระบบ blockchain    
    def create_block(self,nonce,previous_hash):
        #เก็บส่วนประกอบของแต่ละ block id,timestamp,prev_hash
        #blockคือ object dictionary
        block={
            "index":len(self.chain)+1,
            "timestamp":str(datetime.datetime.now()),
            "nonce":nonce,
            "data":self.transaction,
            "previous_hash":previous_hash            
        }
        self.chain.append(block)
        return block
    
    # method ที่ให้บริการเกี่ยวกับ Block ก่อนหน้า
    def get_previous_block(self):
        return self.chain[-1]
    
    # method การเข้ารหัส block
    def hash(self,block):      
        #เตรียมพร้อม data
        encode_block = json.dumps(block,sort_keys=True).encode() # แปลง python object(dict) เป็น json เพื่อเรียงข้อมูลง่ายๆ
        #sha-256
        return hashlib.sha256(encode_block).hexdigest() # hexdigest ทำให้เป็น base16

    # method pow
    def proof_of_work(self,previous_nonce):
        # อยากได้ค่า nonce ที่ส่งผลให้ได้ target hash => 4หลักแรก => 0000xxxx
        new_nonce=1 # ค่า nonce ที่ต้องการ
        check_proof= False #ตัวแปรเช็คค่า nonce ให้ได้ตาม target ที่กำหนด
        # แก้โจทย์ทางคณิตศาสตร์
        while check_proof is False:
            # เลขฐาน16มา1ชุด
            hashoperation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hashoperation[:4] =="0000":
                check_proof=True
            else:
                new_nonce+=1
        return new_nonce


    # ตรวจสอบ block
    def is_chain_valid(self,chain):
        previous_block = chain[0]
        block_index = 1
        while block_index<len(chain):
            block = chain[block_index] # block that check now
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_nonce = previous_block["nonce"] # nonce previous block
            nonce = block["nonce"] # nonce of block that check now
            hashoperation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hashoperation[:4] != "0000":
                return False
            previous_block = block
            block_index += 1
        return True
    
    def new_transaction(self,match,team_a,team_b):
        data = {
            'Match' : match,
            'Team A' : team_a,
            'Team B' : team_b
        }
        self.transaction.append(data)
        return self.get_previous_block['index'] + 1
 

GlobalChain = Blockchain()         
# web server
app = Flask(__name__)

# เริ่มใช้งาน blockchain

blockchain = Blockchain() # สร้างเป็น object ใช้งาน class Blockchain

# routing
@app.route('/')
def hello():
    return "<p>Hello Blockchain</p>"

@app.route('/get_chain',methods=["GET"])
def get_chain():
    response = {
        "chain":blockchain.chain, # ดึง chain มาจาก obj blockchain property chain
        "length":len(blockchain.chain) # ดึง length มา
    }
    return jsonify(response),200 # response ไปแบบ json

@app.route('/mining',methods=["GET"])
def mining_block():
    amount = 1000000 # จำนวนเงินในการทำธุรกรรม
    blockchain.transaction = blockchain.transaction+amount
    #pow
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block["nonce"]
    #nonce
    nonce = blockchain.proof_of_work(previous_nonce)
    #prev hash
    previous_hash = blockchain.hash(previous_block)
    #update new block 
    block = blockchain.create_block(nonce,previous_hash)
    response = {
        "data":block["data"],
        "message":"Mining Block finally!!!",
        "index":block["index"],
        "timestamp":block["timestamp"],
        "nonce":block["nonce"],
        "previous_hash":block["previous_hash"]
    }
    return jsonify(response),200
   
@app.route('/is_valid',methods=["GET"])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response={"message":"Blockchain is Valid"}
    else:
        response={"message":"Blockchain is not Valid"}
    return   jsonify(response),200
 
 
@app.route('/append_transaction',methods=["POST"])
def append_tx():
    amount = 1000000 # จำนวนเงินในการทำธุรกรรม
    blockchain.transaction = blockchain.transaction+amount
    #pow
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block["nonce"]
    #nonce
    nonce = blockchain.proof_of_work(previous_nonce)
    #prev hash
    previous_hash = blockchain.hash(previous_block)
    #update new block 
    block = blockchain.create_block(nonce,previous_hash)
    response = {
        "data":block["data"],
        "message":"Mining Block finally!!!",
        "index":block["index"],
        "timestamp":block["timestamp"],
        "nonce":block["nonce"],
        "previous_hash":block["previous_hash"]
    }
    return jsonify(response),200
    
# run server
if __name__ == "__main__":
    app.run()

blockchain = Blockchain()
t1 = blockchain.new_transaction("1","EVOS Esports","PSG Esports")