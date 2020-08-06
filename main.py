from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import NumericProperty,ColorProperty,ReferenceListProperty,BoundedNumericProperty, ListProperty,StringProperty
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
import random
import time
from kivy.uix.popup import Popup
from kivy.factory import Factory
#from kivy.lang import Factory
Window.size = (320,640)

class Manager(ScreenManager):
	pass
class Menu(Screen):
	def on_enter(self, *args):
		if self.manager.has_screen('game'):
			Clock.unschedule(self.manager.get_screen('game').putBlock)
			self.manager.get_screen('game').LVL_DESIGN = []
			self.manager.get_screen('game').refresh()
			self.manager.get_screen('levels').on_refresh()
class Level(Screen):
	def on_enter(self, *args):
		for x in range(1,10):
			self.spawn = Factory.Menus(text=str(x))
			self.ids.lvl_button.add_widget(self.spawn)
	def on_refresh(self, *args):
		self.ids.lvl_button.clear_widgets()
	def pars(self, texts):
		if texts == '1':
			Level_1 = [
			[False],[True, [1,0,0,1]],[True, [1,0,0,1]],[False],[True, [1,0,0,1]],[True, [1,0,0,1]],[False],
			[True, [1,0,0,1]],[False],[False],[True, [1,0,0,1]],[False],[False],[True, [1,0,0,1]],
			[True, [1,0,0,1]],[False],[False],[False],[False],[False],[True, [1,0,0,1]],
			[False],[True, [1,0,0,1]],[False],[False],[False],[True, [1,0,0,1]],[False],
			[False],[False],[True, [1,0,0,1]],[False],[True, [1,0,0,1]],[False],[False],
			[False],[False],[False],[True, [1,0,0,1]],[False],[False],[False],
			]
			self.manager.get_screen('game').LVL_DESIGN = Level_1
			self.manager.current = 'game'
		elif texts == '2':
			Level_2 = [
			[True, [1,0,0,1]],[True, [0,1,0,1]],[False],[True, [0,1,1,1]],[True, [1,1,0,1]],[False],
			[True, [1,0,0,1]],[False],[False],[True, [1,0,0,1]],[False],[False],[True, [1,0,0,1]],
			[True, [1,0,0,1]],[False],[False],[False],[False],[False],[True, [1,0,0,1]],
			[True, [1,0,0,1]],[False],[False],[False],[True, [1,0,0,1]],[False],
			[True, [1,0,0,1]],[False],[True, [1,0,0,1]],[False],[False],
			[True, [1,0,0,1]],[False],[False],[False],
			]
			self.manager.get_screen('game').LVL_DESIGN = Level_2
			self.manager.current = 'game'
		
		
class Game(Screen):
	LVL_DESIGN = []
	
	color_pattern = [
	[1,0,0,1],
	[0,1,0,1],
	[0,0,1,1],
	[1,0,0,1],
	[1,1,0,1],
	[1,0,1,1],
	[1,1,0,1],
	[0,1,0,1],
	[0,1,1,1],
	[1,0,1,1],
	[0,1,1,1],
	[0,0,1,1],
	]
	

	SCORE = NumericProperty(0)
	LabelScore = NumericProperty(0)
	#GAMEOVER = Pause()
	def on_enter(self, *args):
		self.SCORE = 0
		self.LabelScore = 0
		self.PIXEL = []
	
		self.FALSE_PIXEL = []
		self.TRUE_PIXEL = []
		self.id_button = 0
		self.title = 'fsd'
		self._Block = []
		
		self.desing_lvl()
		#self.root.Pause().open()
		#GameOver(title = self.title).open()
		Clock.schedule_interval(self.putBlock, 1/2)
		Clock.schedule_interval(self.hero_collides, 1/30)
		Clock.schedule_interval(self.update, 1/60)
		#Clock.schedule_interval(self.refresh, 4)
		#Clock.schedule_interval(self.desing_lvl, 8)				
		#def gameo(self, *args):
		
	def desing_lvl(self, *args):

		self.SCORE = 0
		self.LabelScore = 0
		self.PIXEL = []
	
		self.FALSE_PIXEL = []
		self.TRUE_PIXEL = []
		self.id_button = 0
		
		self._Block = []

		for x in self.LVL_DESIGN:
			if x[0]:
				self.buttone = Factory.Pixel()
				self.ids.glem.add_widget(self.buttone)
				self.PIXEL.append(self.buttone)
				self.TRUE_PIXEL.append([self.buttone, x[1]])
				#print(self.TRUE_PIXEL[0][0])
			else:
				self.buttone = Factory.Pixel()
				
				self.PIXEL.append(self.buttone)
				self.ids.glem.add_widget(self.buttone)
				self.FALSE_PIXEL.append(self.buttone)
		#time.sleep(1)
		#print('fsdf')
	#РЕСТАРТ
	def refresh(self, *args):
		self.ids.glem.clear_widgets()
		for blc in range(0,len(self._Block)):
			self.remove_widget(self._Block[blc])

			
			
	
	#ПАУЗА
	def on_pause(self):
		Clock.unschedule(self.putBlock, 1/2)
		Clock.unschedule(self.hero_collides, 1/30)
		Clock.unschedule(self.update, 1/60)			

		
		
	# ОТЖАТИЕ ПАУЗЫ
	def un_pause(self):
		Clock.schedule_interval(self.putBlock, 1/2)
		Clock.schedule_interval(self.hero_collides, 1/30)
		Clock.schedule_interval(self.update, 1/60)						
	
	
	
	#ПЕРЕДВИЖЕНИЕ
	def on_touch_move(self, touch):
		if touch.x >= self.ids.hero.x - 50 and \
			touch.x <= self.ids.hero.x + self.ids.hero.width + 50:
			if touch.x <= Window.width - 40 and touch.x >= 0:
				self.ids.hero.x = touch.x
				
				

	#ОБНОВЛЕНИЕ ИГРЫ	
	def update(self, *args):
		#self.on_pause()
		#GameOver().open()
		for block in self._Block:
			if block.y >= 0:
				block.y -= 5
			else:
				self.remove_widget(block)
				self._Block.remove(block)		
				
		if self.id_button < len(self.TRUE_PIXEL):
			self.ids.nextcolor.background_color = self.TRUE_PIXEL[int(self.id_button)][1]
		else:
			self.on_pause()
			#GameOver(title = self.title).open()
			
			
	#КАЛИЗИЯ 	
	def collided(self,wid1,wid2):
		#print('fds')
		if wid2.x <= wid1.x + wid1.width and \
			wid2.x + wid2.width > wid1.x and \
			wid2.y <= wid1.y + wid1.height and \
			wid2.y + wid2.height >= wid1.y:
			return True
		else:
			return False	
			
			
	#КОЛИЗИЯ ИГРОКА		
	def hero_collides(self,*args):
		color = ColorProperty(['1', '1', '1', '1'])
		for block in self._Block:
			if self.collided(self.ids.hero,block):
				if block.point:
					block.point = False
					if self.id_button < len(self.TRUE_PIXEL):
						if self.TRUE_PIXEL[int(self.id_button)][1] == block.color:
							self.SCORE += 1
							self.LabelScore = float('{0:.1f}'.format((self.SCORE / len(self.TRUE_PIXEL)) * 100))
						self.TRUE_PIXEL[int(self.id_button)][0].background_color = block.color
						self.id_button += 1
						self.remove_widget(block)
						self._Block.remove(block)
					else: 
						print('GAME OVER')
	
	#СПАВН БЛОКА
	def putBlock(self,*args):
		#self.scored = False
		block = Block(y=self.height, x=random.randint(0,self.width), color = random.choice(self.color_pattern))
		self.add_widget(block)
		self._Block.append(block)	

class LevelButton(Button):
	pass
class Pause(Popup):	
	pass
class GameOver(Popup):
	title = StringProperty()
		
class Hero(Image):
	pass
	
class Block(Widget):
	color = ColorProperty(['1', '1', '1', '1'])
	point = True
		
class Main(App):
	pass

if __name__ == '__main__':
	Main().run()