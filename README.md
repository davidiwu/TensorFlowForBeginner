# TensorFlow For Beginner

demonstrate how to use Google's TensorFlow for absolute beginner


# Prepare for Windows OS

1. Check your Windows system, should be Windows 7 or later, and 64-bit operating systems.
	
	TensorFlow was built and tested on 64-bit laptop/desktop operating system.
    
2. Download and install the latest version of Python (3.6.3 as of Nov 10th 2017) for Windows.
    
	Should select to download 64bit version of Python 
    
3. Install TensorFlow in a command line run as administrator:
    
	To install the CPU-only version of TensorFlow, enter the following command:
    
	C:\> pip3 install --upgrade tensorflow


	To install the GPU version of TensorFlow, enter the following command:
    
	C:\> pip3 install --upgrade tensorflow-gpu
	
4. Install Visual Studio Code as Python IDE.


# TensorFlow Terminology

Graph:

	A computational graph is a series of TensorFlow operations arranged into a graph of nodes.
	
Nodes:

	Each node takes zero or more tensors as inputs and produces a tensor as an output
	
	A constant is a type of node, it takes no inputs, and it outputs a value it stores internally
	
	A operation is also a node, like 'add' operation
	
Placeholders:

	A graph can be parameterized to accept external inputs, known as placeholders.
	A placeholder is a promise to provide a value later
	
	we can use feed_dict argument to the 'run' method to feed concrete values to the placeholders
	
		a = tf.placeholder(tf.float32)
		b = tf.placeholder(tf.float32)
		adder_node = a + b  # + provides a shortcut for tf.add(a, b)
		print(sess.run(adder_node, {a: 3, b: 4.5}))
		print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))
	
Variables:

	In machine learning we will typically want a model that can take arbitrary inputs, such as the one above. 
	To make the model trainable, we need to be able to modify the graph to get new outputs with the same input. 
	Variables allow us to add trainable parameters to a graph. They are constructed with a type and initial value.
	
		W = tf.Variable([.3], dtype=tf.float32)
		b = tf.Variable([-.3], dtype=tf.float32)
		x = tf.placeholder(tf.float32)
		linear_model = W*x + b
	
	Variables are not initialized when you call tf.Variable. 
	To initialize all the variables in a TensorFlow program, you must explicitly call a special operation as follows:
	
		init = tf.global_variables_initializer()
		sess.run(init)
		
	It is important to realize init is a handle to the TensorFlow sub-graph that initializes all the global variables. 
	Until we call sess.run, the variables are uninitialized.
	
	
	
	
