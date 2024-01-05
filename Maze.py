import os
import keyboard
import time


class Stack:

    def __init__(self):
        self._top = None
        self._size = 0
        #สร้าง Stack ว่างๆ โดยกำหนด _top เป็น None และ _size เป็น 0

    def isEmpty(self):
        return self._top is None
        # ตรวจสอบว่า Stack ว่างหรือไม่ โดยเช็คว่า _top มีค่าเป็น None หรือไม่.
    
    def __len__(self):
        return self._size
        #คืนค่าขนาดของ Stack โดยใช้ค่า _size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item
        #คืนค่าข้อมูลที่อยู่ที่ด้านบนของ Stack โดยไม่ลบข้อมูลนั้นออกจาก Stack (เหมือนการดูข้อมูลด้านบน).

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size = self._size - 1
        return node.item
        #นำข้อมูลที่อยู่ที่ด้านบนของ Stack ออกและคืนค่าข้อมูลนั้น.

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size = self._size + 1
        # เพิ่มข้อมูลลงใน Stack ที่ด้านบน.

class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link
        #ถูกใช้เพื่อเก็บข้อมูลและลิงก์ไปยัง Node ถัดไปใน Stack:


class maze:#คลาสที่เกี่ยวกับเขาวงกต
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        #ลิสต์ที่มีลิสต์ซ้อนอยู่ภายใน เป็นโครงสร้างของแผนที่ที่เก็บข้อมูลเรื่องการวาดตำแหน่งของ "P" (ผู้เล่น), "E" (ทางออก), "X" (ขอบของแผนที่), และช่องว่าง " " (ทางเดินที่ผู้เล่นสามารถเคลื่อนที่ได้).
        self.ply = pos(5, 1)#การสร้างอ็อบเจกต์ pos ที่มีตำแหน่งเริ่มต้นที่ (คอลัมที่5-y-, แถวที่1-x-) และกำหนดให้ self.ply เก็บ อ้างอิง ไปยังอ็อบเจกต์นี้. ตำแหน่งนี้จะถูกใช้เพื่อตำแหน่งเริ่มต้นของผู้เล่นในแผนที่.
        self.end = pos(2, 6)#การสร้างอ็อบเจกต์ pos ที่มีตำแหน่งที่ (คอลัมที่2-y-, แถวที่6-x-) และกำหนดให้ self.end เก็บ อ้างอิง ไปยังอ็อบเจกต์นี้. ตำแหน่งนี้จะถูกใช้เพื่อตำแหน่งของทางออกในแผนที่.
        self.maze[self.ply.y][self.ply.x] = "P"#"P": นี้คือการให้ตำแหน่งที่ผู้เล่นเริ่มต้น (ตำแหน่ง self.ply) ในแผนที่มีค่าเป็น "P" (ตัวแทนของผู้เล่น).
        self.maze[self.end.y][self.end.x] = "E"#"E": นี้คือการให้ตำแหน่งที่ทางออก (ตำแหน่ง self.end) ในแผนที่มีค่าเป็น "E" (ตัวแทนของทางออก).
    
    def isInBound(self, y, x):#isInBound เป็นเมธอดที่ถูกนิยามในคลาส mazeซึ่งใช้เพื่อตรวจสอบว่าตำแหน่งที่กำหนดด้วย y และ x นั้นอยู่ภายในขอบเขตของแผนที่หรือไม่
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
        # y>=0 and x>=0 มีค่าไม่น้อยกว่า 0 (ต้องเป็นตำแหน่งที่ไม่ต่ำกว่าตำแหน่งนับจากด้านบนของแผนที่).
        # y<len(self.maze) and x<len(self.maze[0])มีค่าน้อยกว่าความยาว (จำนวนแถว) (จำนวนคอลัมน์) ของแผนที่.
            return True # บอกว่าตำแหน่งอยู่ในพื้นที่
        else:
            return False #ตำแหน่งอยู่นอกพื้นที่
    
    def print(self):#ถูกนิยามเพื่อที่จะแสดง (print) แผนที่ในทางที่สะดวกที่สุดในหน้าจอหรือที่อื่น ๆ ที่ระบบสนับสนุนการแสดงผล
        os.system("cls")#ใช้เรียกคำสั่งระบบเพื่อล้างหน้าจอในกรณีที่รันบนระบบปฏิบัติการ Windows คำสั่งที่เหมือนกันสามารถเป็น "clear" แทน.
        print("\n\n\n")#พิมพ์บรรทัดว่างที่ขาดหายไป 3 บรรทัด (เพื่อให้มีช่องว่างข้างบนของแผนที่).
        for row in self.maze:#วนลูปผ่านแถวของแผนที่.
            for col in row:#วนลูปผ่านคอลัมน์ในแถว.
                print(col," ", end="")#พิมพ์ค่าในแต่ละช่องของแผนที่และเว้นวรรคหลังจากทุกค่า.
            print("")#พิมพ์บรรทัดว่างหลังจากทุกแถว.
        print("\n\n\n")#พิมพ์บรรทัดว่างที่ขาดหายไป 3 บรรทัด (เพื่อให้มีช่องว่างข้างล่างของแผนที่).
    
    def printEND(self):#เป็นเมธอดที่ถูกนิยามเพื่อที่จะแสดงข้อความแสดงผลที่แจ้งว่าผู้เล่นได้ถึงทางออกแล้ว (Congratulation). ฟังก์ชันนี้ทำงานเช่นเดียวกับ print แต่มีเพียงข้อความแสดงผลเฉพาะที่เกี่ยวข้องกับการผ่านเกม
        os.system("cls")#ใช้เรียกคำสั่งระบบเพื่อล้างหน้าจอในกรณีที่รันบนระบบปฏิบัติการ Windows คำสั่งที่เหมือนกันสามารถเป็น "clear" แทน.
        print("\n\n\n")#พิมพ์บรรทัดว่างที่ขาดหายไป 3 บรรทัด (เพื่อให้มีช่องว่างข้างบนของแผนที่).
        print(">>>>> Congraturation!!! <<<<<")#แสดงคำว่าCongraturation!!!
        print("\n\n\n")#พิมพ์บรรทัดว่างที่ขาดหายไป 3 บรรทัด (เพื่อให้มีช่องว่างข้างบนของแผนที่).
        keyboard.wait("")#ใช้รอให้ผู้เล่นกดปุ่มใด ๆ บนแป้นพิมพ์ก่อนที่โปรแกรมจะสิ้นสุด 

    def move_up(self):#เป็นเมธอดที่ใช้ในการเคลื่อนที่ของผู้เล่นไปทางบน (ขึ้น) ในแผนที่. 
        next_move = pos(self.ply.y-1, self.ply.x)
        # นี้ถูกใช้เพื่อสร้างอ็อบเจกต์ pos ใหม่ที่อยู่ด้านบนของตำแหน่งปัจจุบันของผู้เล่น 
        #นำค่า y ของตำแหน่งปัจจุบันของผู้เล่นลบด้วย 1 ในแนวตั้ง เพื่อทำให้ได้ตำแหน่งด้านบนของตำแหน่งปัจจุบัน.
        #ใช้ค่า x ของตำแหน่งปัจจุบันของผู้เล่นโดยไม่เปลี่ยนแปลง. self.ply อยู่ที่ตำแหน่ง (2, 3) ในแผนที่, บรรทัดนี้จะสร้าง next_move ที่มีค่า pos(1, 3), ซึ่งคือตำแหน่งด้านบนของตำแหน่งปัจจุบัน.
        if self.isInBound(next_move.y,next_move.x):#ตรวจสอบว่าตำแหน่งด้านบนนั้นอยู่ภายในขอบเขตของแผนที่โดยใช้ isInBound
            if self.maze[next_move.y][next_move.x] == " ":#ถ้าตำแหน่งด้านบนอยู่ภายในขอบเขต, ตรวจสอบว่าตำแหน่งนั้นมีค่าเป็นช่องว่างหรือไม่
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"#ถ้าตำแหน่งนั้นเป็นช่องว่าง, ทำการอัพเดตตำแหน่งผู้เล่นในแผนที่.
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":#ถ้าตำแหน่งนั้นเป็นตำแหน่งของทางออก ("E"), ให้เรียกฟังก์ชัน printEND เพื่อแสดงข้อความแสดงผลการผ่านเกมและจบการทำงานของโปรแกรม.
                self.printEND()
                return False#ถ้ามีเงื่อนไขใดเงื่อนไขหนึ่งไม่เป็นจริง, ส่งค่ากลับ False เพื่อบ่งบอกว่าการเคลื่อนที่ไม่สามารถทำได้.
        return True#ส่งค่ากลับ True เพื่อบ่งบอกว่าการเคลื่อนที่ประสบความสำเร็จ.
    
    def move_down(self):#ช้ในการเคลื่อนที่ผู้เล่นลง (ทางล่าง) ในแผนที่
        next_move = pos(self.ply.y+1, self.ply.x)#สร้างอ็อบเจกต์ pos ใหม่ที่อยู่ด้านล่างของตำแหน่งปัจจุบันของผู้เล่น
        #self.ply.y + 1: นำค่า y ของตำแหน่งปัจจุบันของผู้เล่นบวกด้วย 1 ในแนวตั้ง เพื่อทำให้ได้ตำแหน่งด้านล่างของตำแหน่งปัจจุบัน.
        #self.ply.x: ใช้ค่า x ของตำแหน่งปัจจุบันของผู้เล่นโดยไม่เปลี่ยนแปลง.
        #self.ply อยู่ที่ตำแหน่ง (2, 3) ในแผนที่, บรรทัดนี้จะสร้าง next_move ที่มีค่า pos(3, 3), ซึ่งคือตำแหน่งด้านล่างของตำแหน่งปัจจุบัน.
        if self.isInBound(next_move.y,next_move.x):#ตรวจสอบว่าตำแหน่งด้านล่างนั้นอยู่ภายในขอบเขตของแผนที่โดยใช้ isInBound
            if self.maze[next_move.y][next_move.x] == " ":#ถ้าตำแหน่งด้านล่างอยู่ภายในขอบเขต, ตรวจสอบว่าตำแหน่งนั้นมีค่าเป็นช่องว่างหรือไม่.
                self.maze[self.ply.y][self.ply.x] = " "#ถ้าตำแหน่งนั้นเป็นช่องว่าง
                self.maze[next_move.y][next_move.x] = "P"# ทำการอัพเดตตำแหน่งผู้เล่นในแผนที่.
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":#ถ้าตำแหน่งนั้นเป็นตำแหน่งของทางออก ("E"), 
                self.printEND()#ให้เรียกฟังก์ชัน printEND เพื่อแสดงข้อความแสดงผลการผ่านเกมและจบการทำงานของโปรแกรม.
                return False#ถ้ามีเงื่อนไขใดเงื่อนไขหนึ่งไม่เป็นจริง, ส่งค่ากลับ False เพื่อบ่งบอกว่าการเคลื่อนที่ไม่สามารถทำได้.
        return True#ส่งค่ากลับ True เพื่อบ่งบอกว่าการเคลื่อนที่ประสบความสำเร็จ.

    def move_left(self):# ใช้ในการเคลื่อนที่ผู้เล่นไปทางซ้ายในแผนที่.
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

if __name__ == '__main__':

    m = maze()#สร้างแผนที่
    m.print()#ปีิ้นแผนที่
    stack = Stack()
    
    # m.move_up()
    # m.print()
    # print(m.ply.x, m.ply.y)
    # input()

    # m.move_up()
    # m.print()
    # print(m.ply.x, m.ply.y)
    # input()

    while True:
        print(m.ply.y, m.ply.x)
        if m.move_up():
            m.maze[m.ply.y][m.ply.x-1] == " "
            m.maze[m.ply.y][m.ply.x] = "P"
            m.move_up()
            time.sleep(0.25)
            m.print()
        elif m.move_up() and m.maze[m.ply.y][m.ply.x-1] == "X":
            m.move_down()
            move_left() and m.maze[m.ply.y][m.ply.x-1]
            



        
            




        
        # if 
        #     m.maze[next_move.y][next_move.x] == " "
        #     m.maze[m.ply.y][m.ply.x] = " "
        #     m.maze[m.next_move.y][m.next_move.x] = "P"
        #     m.ply = move_up
        #     time.sleep(0.25)
        # else:
        #     m.maze[next_move.y][next_move.x] == "X":

        




            

    #m.move_up()
    #m.print()
    #input()

  

    # while True:
    #     if keyboard.is_pressed("q"):
    #         print("Quit Program")
    #         break
    #     if keyboard.is_pressed("w"):
    #         if m.move_up():
    #             m.print()
    #         else:
    #             break
    #     if keyboard.is_pressed("s"):
    #         if m.move_down():
    #             m.print()
    #         else:
    #             break
    #     if keyboard.is_pressed("a"):
    #         if m.move_left():
    #             m.print()
    #         else:
    #             break
    #     if keyboard.is_pressed("d"):
    #         if m.move_right():
    #             m.print()
    #         else:
    #             break