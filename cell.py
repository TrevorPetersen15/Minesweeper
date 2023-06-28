from tkinter import Button
import random 

GRID_SIZE=6
MINES_COUNT=(GRID_SIZE**2)//4


class Cell:
    all=[]
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.x = x
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

    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surronded_cells_mines_length==0:
                for cell in self.surronded_cells:
                    cell.show_cell() 
            self.show_cell()
            
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
        self.cell_btn_object.configure(text=self.surronded_cells_mines_length) 
               
    def show_mine(self):
        self.cell_btn_object.config(bg="red")

    def right_click_actions(self,event):
        print ("right click")
        
    @staticmethod
    def radommize_mines():
        picked_cells=random.sample(Cell.all,MINES_COUNT)
        
        for picked_cell in picked_cells:
                picked_cell.is_mine=True
                
    def __repr__(self):
        return f"cell({self.x}),({self.y})"