import tkinter as tk
from tkinter import messagebox

class HexCypher: 
    
    @classmethod

    def encode(cls, s:str, n:str) -> str:
        result = s 
        for _ in range(int(n)):
            result = result.encode('utf-8').hex()
        return result
    

    @classmethod

    def decode(cls, s:str, n:str) -> str:
        result = s 
        for _ in range(int(n)):
            result = bytes.fromhex(result).decode('utf-8')
        return result 
    

def process_action():
    text = textEntry.get()
    times = timesHex.get()
    operation = mode_var.get()

    if not text or not times: 
        messagebox.showwarning("Missing input", "Please fill in both text and times.")
        return
    
    cypher = HexCypher()

    if operation == "encode":
        result = cypher.encode(text, times)
    else: 
        result = cypher.decode(text,times)

    output_entry.delete(0, tk.END)
    output_entry.insert(0, result)



root = tk.Tk()
root.title("hex-cypher")
root.geometry("450x200")
root.wm_attributes('-alpha', 0.85)
root.resizable(width=False, height=False)

tk.Label(root, text="text:").grid(row=0,column=0,sticky="e",padx=5,pady=5)
textEntry = tk.Entry(root,width=60)
textEntry.grid(row=0,column=1,padx=5)

tk.Label(root,text="times:").grid(row=1,column=0,sticky="e",padx=5,pady=5)
timesHex = tk.Entry(root,width=60)
timesHex.grid(row=1,column=1,padx=5)

mode_var = tk.StringVar(value="encode")
tk.Label(root,text="mode:").grid(row=2,column=0,sticky="e")
tk.Radiobutton(root, text="encode", variable=mode_var, value="encode").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="decode", variable=mode_var, value="decode").grid(row=2, column=1, padx=100, sticky="w")

tk.Button(root, text="process", command=process_action, width=20).grid(row=4, column=1, pady=10)

tk.Label(root, text="result:").grid(row=5, column=0, sticky="e", padx=5)
output_entry = tk.Entry(root, width=60)
output_entry.grid(row=5, column=1, padx=5)

root.mainloop()