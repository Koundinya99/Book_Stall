class Book_Stall():
    def __init__(self,b='',c='',d='',e='',f='',g='',h='',price=0,q=0):
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
        self.g=g
        self.h=h
        self.price=price
        self.q=q
        
        
    def Horror(self):
        print('   AUTHOR                 BOOK                   PRICE')
        print('--------------------------------------------------------')
        print('1.Mark Z Daniel:     House of LeavesMark\t  $30')
        print('2.Mary Shelley:      Frankstein\t\t\t  $39')
        print('3.Bram Stoker:       Dracula\t\t\t  $40')
        print('4.Stephen King:      The Shining\t\t  $45')
        print('5.Paul Trembley:     Head Full of Ghosts\t  $69\n\n')
        
 #=============================================================================
        while True:
           print('For main menu click 0') 
           b=int(input('To choose any book from HORROR, enter a number from 1-5: '))
           if b==1:
               print("\nYou've chosen 'HOUSE OF THE LEAVES' by 'MARK Z DANIEL'")
               q=int(input('Quantity: '))
               print('Cost: $',q*30)
               self.q=self.q+q*30    
         
           if b==2:
               print("\nYou've chosen 'FRANKSTEIN' by 'MARK SHELLEY'")
               q=int(input('Quantity: '))
               print('Cost: $',q*39)
               self.q=self.q+q*39  
             
           if b==3:
               print("\nYou've chosen 'DRACULA' by 'BRAM STOKER'")
               q=int(input('Quantity: '))
               print('Cost: $',q*40)
               self.q=self.q+q*40  
             
           if b==4:
               print("\nYou've chosen 'THE SHINING' by 'STEPHEN KING'")
               q=int(input('Quantity: '))
               print('Cost: $',q*45)
               self.q=self.q+q*45  
             
           if b==5:
               print("\nYou've chosen 'HEAD FULL OF GHOSTS' by 'PAUL TREMBLEY'")
               q=int(input('Quantity: '))
               print('Cost: $',q*69)
               self.q=self.q+q*69      
          
           if b<1 or b>6:
               break
     
 
    def Romance(self):
        print('   AUTHOR                 BOOK                   PRICE')
        print('--------------------------------------------------------')
        print('1.Jane Austen\t\tPride and Prejudice\t  $33')
        print('2.Nicholas Sparks\tThe Notebook\t\t  $40')
        print('3.Margaret Mitchell\tGone with the wind\t  $56')
        print('4.Diana Gabaldon\tOutlander\t\t  $55')
        print("5.Koundinya\t\tIt's First Love\t\t  $100\n\n")
        
 #=============================================================================
        while True:
           print('For main menu click 0')
           b=int(input('To choose any book from ROMANCE, enter a number from 1-5: '))
           if b==1:
               print("\nYou've chosen 'PRIDE AND PREJUDICE' by 'JANE AUSTEN'")
               q=int(input('Quantity: '))
               print('Cost: $',q*33)
               self.q=self.q+q*33    
         
           if b==2:
               print("\nYou've chosen 'THE NOTEBOOK' by 'NICHOLAS SPARKS'")
               q=int(input('Quantity: '))
               print('Cost: $',q*40)
               self.q=self.q+q*40  
             
           if b==3:
               print("\nYou've chosen 'GONE WITH THE WIND' by 'MARGARET MITCHELL'")
               q=int(input('Quantity: '))
               print('Cost: $',q*56)
               self.q=self.q+q*56  
             
           if b==4:
               print("\nYou've chosen 'OUTLANDER' by 'DIANA GABALDON'")
               q=int(input('Quantity: '))
               print('Cost: $',q*55)
               self.q=self.q+q*55  
             
           if b==5:
               print("\nYou've chosen 'IT'S FIRST LOVE' by KOUNDINYA")
               q=int(input('Quantity: '))
               print('Cost: $',q*100)
               self.q=self.q+q*100      
          
           if b<1 or b>6:
               break
     
 
    def Wild_Life(self):
        print('   AUTHOR                 BOOK                   PRICE')
        print('--------------------------------------------------------')
        print('1.Lawrence Anthony\tThe Elephant Whisperer    $50')
        print('2.Lucy Cooke\t\tThe Truth about Animals\t  $39')
        print('3.Michael Jordan\tGorillas in the Mist\t  $67')
        print('4.Deila Clinton\t\tCry of the Kalahari\t  $59')
        print('5.Paul Sterry\t\tBritish Wildlife\t  $70\n\n')
   
        while True:
           print('For main menu click 0') 
           b=int(input('To choose any book from WILDLIFE, enter a number from 1-5: '))
           if b==1:
               print("\nYou've chosen 'THE ELEPHANT WHISPERER' by 'LAWRENCE ANTHONY'")
               q=int(input('Quantity: '))
               print('Cost: $',q*50)
           self.q=self.q+q*50    
         
           if b==2:
               print("\nYou've chosen 'THE TRUTH ABOUT ANIMALS' by 'LUCY COOKE'")
               q=int(input('Quantity: '))
               print('Cost: $',q*39)
           self.q=self.q+q*39  
             
           if b==3:
               print("\nYou've chosen 'GORILLAS IN THE MIST' by 'MICHAEL JORDAN'")
               q=int(input('Quantity: '))
               print('Cost: $',q*67)
           self.q=self.q+q*67  
             
           if b==4:
               print("\nYou've chosen 'CRY OF THE KALAHARI' by 'DEILA CLINTON'")
               q=int(input('Quantity: '))
               print('Cost: $',q*59)
           self.q=self.q+q*59  
             
           if b==5:
               print("\nYou've chosen 'BRITISH WILDLIFE' by 'PAUL STERRY'")
               q=int(input('Quantity: '))
               print('Cost: $',q*70)
           self.q=self.q+q*70      
          
           if b<1 or b>6:
               break
     
    def Author(self):
        print('\t\tBooks authored by KOUNDINYA')
        print('---------------------------------------------------------') 
        print('   AUTHOR                 BOOK                   PRICE')
        print('---------------------------------------------------------') 
        print('1.Koundinya\t  Traits of an Introvert\t  $50')
        print('2.Koundinya\t  The Memor of an Unborn Child\t  $70')
        print('3.Koundinya\t  The Ruthless Dictator\t\t  $170')
        print('4.Koundinya\t  The Saloon\t\t\t  $50')
        print('5.Koundinya\t  Tussle\t\t\t  $50')

        while True:
           print('For main menu click 0') 
           b=int(input('To choose any book authored by KOUNDINYA, enter a number from 1-5: '))
           if b==1:
               print("\nYou've chosen 'TRAITS OF AN INTROVERT'")
               q=int(input('Quantity: '))
               print('Cost: $',q*50)
               self.q=self.q+q*50    
         
           if b==2:
               print("\nYou've chosen 'THE MEMOR OF AN UNBORN CHILD'")
               q=int(input('Quantity: '))
               print('Cost: $',q*70)
               self.q=self.q+q*70  
             
           if b==3:
               print("\nYou've chosen 'DICTATOR'")
               q=int(input('Quantity: '))
               print('Cost: $',q*170)
               self.q=self.q+q*170  
             
           if b==4:
               print("\nYou've chosen 'THE SALOON'")
               q=int(input('Quantity: '))
               print('Cost: $',q*50)
               self.q=self.q+q*50  
             
           if b==5:
               print("\nYou've chosen 'TUSSLE'")
               q=int(input('Quantity: '))
               print('Cost: $',q*50)
               self.q=self.q+q*50      
          
           if b<1 or b>6:
               break
             
    def tot_bill(self):
        print('Total Bill: $',self.q)

BS=Book_Stall()
# BS.Horror() 
# BS.Romance()  
# BS.Wild_Life()     
# BS.Author()
while True:
  print('----------------------------------------------------------------------')
  print('\t\t\tB O O K   M E L A\n');print('The following genre are available')
  print('\n1.Books authored by Koundinya')
  print('2.Romance')
  print('3.Horror')
  print('4.WildLife')
  print('5.Billing\n')  
  print('To exit, click 0')
  a=int(input('To select any genre, enter a number from 1-5: '))
  print('\n')
  if a==1:
      BS.Author()
  elif a==2:
      BS.Romance()
  elif a==3:
      BS.Horror()
  elif a==4:
      BS.Wild_Life()
  elif a==5:
      BS.tot_bill()
      print('Thanks for shopping.')
      break
  elif a==0:
      print('Re-enter')  
      break















