#!/usr/bin/env python
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

import roslib; roslib.load_manifest('behavior_hello_world_demo')
from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.wait_state import WaitState
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Jul 23 2017
@author: Dennis Chen
'''
class HelloWorldDemoSM(Behavior):
	'''
	Behavior created during in the FlexBE tutorial.
	'''


	def __init__(self):
		super(HelloWorldDemoSM, self).__init__()
		self.name = 'Hello World Demo'

		# parameters of this behavior
		self.add_parameter('waiting_time', 1)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:

		# O 215 104 
		# This is FlexBE tutorial.



	def create(self):
		hello = "Hello World!"
		# x:99 y:341, x:183 y:388
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:86 y:95
			OperatableStateMachine.add('Initial_Wait',
										WaitState(wait_time=self.waiting_time),
										transitions={'done': 'Print_Greeting'},
										autonomy={'done': Autonomy.Off})

			# x:79 y:209
			OperatableStateMachine.add('Print_Greeting',
										LogState(text=hello, severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.High})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
