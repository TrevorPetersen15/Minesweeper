from tkinter import Button ,Label
import random 
import ctypes
import sys
GRID_SIZE=6
CELL_COUNT= GRID_SIZE**2
MINES_COUNT=(GRID_SIZE**2)//4


class Cell:
    cell_count_label_object=None
    all=[]
    cell_count=CELL_COUNT
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.x = x
        self.is_opened = False
        self.flagged = False
        self.y = y
        self.cell_btn_object= None
        
        #############appending obejecting to the cell.all is#########################
        Cell.all.append(self)
        

    def create_btn_object(self,location):
        btn = Button(
            location,
            width=8,
            height=3

        )
        btn.bind("<Button-1>",self.left_click_actions)
        btn.bind("<Button-3>",self.right_click_actions)

        self.cell_btn_object = btn
        
    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left:{CELL_COUNT-MINES_COUNT}" ,
            width= 12,
            height=3,
            font=("",20) 
        )
        Cell.cell_count_label_object = lbl   
    
            

    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surronded_cells_mines_length==0:
                for cell in self.surronded_cells:
                    cell.show_cell() 
            self.show_cell()
            # 
            if Cell.cell_count== MINES_COUNT:
                cell.show_cell()
                ctypes.windll.user32.MessageBoxW(0,"YOU HAVE WON","GAME OVER",0)
        
        self.cell_btn_object.unbind("Button-1")
        self.cell_btn_object.unbind("Button-3")

            
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @property       
    def surronded_cells(self):
        cells=[
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
            ]
        
        cells=[cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surronded_cells_mines_length(self):
        counter=0
        for cell in self.surronded_cells:
            if cell.is_mine:
                counter+=1
        return counter
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -=1
            self.cell_btn_object.configure(text=self.surronded_cells_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left:{Cell.cell_count}")
            self.cell_btn_object.config(bg="SystemButtonFace")
  
        self.is_opened=True
        
               
    def show_mine(self):
        self.cell_btn_object.config(bg="red")
        ctypes.windll.user32.MessageBoxW(0,'You clicked on a mine', "game over",0)
        sys.exit()
                
    def right_click_actions(self,event):
        if not self.flagged:
            self.cell_btn_object.config(bg="orange")
            self.flagged=True
        else:
            self.cell_btn_object.config(bg="SystemButtonFace")
            self.flagged=False
        
            
        
    @staticmethod
    def radommize_mines():
        picked_cells=random.sample(Cell.all,MINES_COUNT)
        
        for picked_cell in picked_cells:
                picked_cell.is_mine=True
                
    def __repr__(self):
        return f"cell({self.x}),({self.y})"