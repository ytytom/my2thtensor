# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

state = tf.Variable(0,name='counter')
# 创建一个变量, 初始化为标量 0.
#Variable 也是变量的意思
'''
    tf.Variable(initial_value=None, trainable=True, collections=None, validate_shape=True, 
    caching_device=None, name=None, variable_def=None, dtype=None, expected_shape=None, 
    import_scope=None)
'''


one = tf.constant(1)
#常量1 tensorflow里常量变量都要用tensor的形式才能参与运算



new_value = tf.add(state, one)
#定义一个add的运算，参与运算的是state和one这两个tensor

update = tf.assign(state, new_value)
#定义个更新的tensor tf.assign是用 后面的参数更新前面的参数。。。
"""
tf.assign(ref, value, validate_shape=None, use_locking=None, name=None)

    Update 'ref' by assigning 'value' to it.

  This operation outputs a Tensor that holds the new value of 'ref' after
    the value has been assigned. This makes it easier to chain operations
    that need to use the reset value.

  Args:
    ref: A mutable `Tensor`.
      Should be from a `Variable` node. May be uninitialized.
    value: A `Tensor`. Must have the same type as `ref`.
      The value to be assigned to the variable.
    validate_shape: An optional `bool`. Defaults to `True`.
      If true, the operation will validate that the shape
      of 'value' matches the shape of the Tensor being assigned to.  If false,
      'ref' will take on the shape of 'value'.
    use_locking: An optional `bool`. Defaults to `True`.
      If True, the assignment will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` that will hold the new value of 'ref' after
      the assignment has completed.
  """



# init_op = tf.initialize_all_variables()
init_op = tf.global_variables_initializer()

"""
  tf.global_variables_initializer()

  Returns an Op that initializes(初始化) global variables.

  This is just a shortcut for `variables_initializer(global_variables())`

  Returns:
    An Op that initializes global variables in the graph.
  
"""


# 启动图后, 变量必须先经过`初始化` (init) op 初始化,（如果全部是常量就不需要）
# 首先必须增加一个`初始化` op 到图中.


with tf.Session() as sess:
  # 运行 'init' op
    sess.run(init_op)
  # 打印 'state' 的初始值
    print(sess.run(state))
  # 运行 op, 更新 'state', 并打印 'state'
    for _ in range(33):
        #这种循环只是执行33次的意思
        sess.run(update)
        print(sess.run(state))
