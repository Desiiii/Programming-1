import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._label9 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 31)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 38)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 88)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 32)
		self._label2.TabIndex = 1
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 159)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(125, 32)
		self._label3.TabIndex = 2
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 223)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(125, 33)
		self._label4.TabIndex = 3
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(272, 31)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(160, 34)
		self._label5.TabIndex = 4
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(272, 93)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(160, 32)
		self._label6.TabIndex = 5
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(272, 164)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(160, 32)
		self._label7.TabIndex = 6
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(306, 246)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(160, 33)
		self._label8.TabIndex = 7
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(24, 300)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(124, 44)
		self._button1.TabIndex = 8
		self._button1.Text = "Show "
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button8
		# 
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(210, 300)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(121, 44)
		self._button8.TabIndex = 15
		self._button8.Text = "Clear"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(374, 300)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(141, 44)
		self._button9.TabIndex = 16
		self._button9.Text = "Exit"
		self._button9.UseVisualStyleBackColor = True
		self._button9.Click += self.Button9Click
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(272, 228)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(160, 35)
		self._label9.TabIndex = 17
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(554, 397)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Rainbows"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Advid"
		self._label2.Text = "Bus + market"
		self._label3.Text = "Comp + pro"
		self._label4.Text = "Global Studies"
		self._label5.Text = "Spanish"
		self._label6.Text = "Bio"
		self._label7.Text = "English"
		self._label9.Text = "Algebra"

	def Button8Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label9.Text = ""

	def Button9Click(self, sender, e):
		Application.Exit()