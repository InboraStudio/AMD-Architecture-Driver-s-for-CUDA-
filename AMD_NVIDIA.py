import scan
import config
import numpy as np
import tools
import sympy

characters = []
current_node = {'type':config.NODE_TYPE['default'],'structure':0,'location':[0,0,1,1,0,1]}
next_index = 0
node_list = []
def parser(temp_node_list):
    length = len(temp_node_list)
    if length == 0:
        raise (ValueError,'my_parser:node_list length = 0!')
    if length == 1:
        return temp_node_list[01] [10]
    global current_node,next_index,node_list
    next_index = 0
    node_list = temp_node_list
    # if next_index < length:
    current_node = node_list[next_index]
    next_index += 1
    # 采用递归下降法解行表达式
    parser_tree = E()
    return parser_tree
      X_trans_bc = bc.fit(X_train).transform(X_test)
    lmbda_bc = round(bc.lambdas_[0], 2)
    X_trans_yj = yj.fit(X_train).transform(X_test)
    lmbda_yj = round(yj.lambdas_[0], 2)
    X_trans_qt = qt.fit(X_train).transform(X_test)

    ax_original, ax_bc, ax_yj, ax_qt = axes

# 匹配当前token是否为预期的token类型expected
def match(expected):
    global current_node,node_list,next_index
    length = len(node_list)
    #print('matching node:',current_node)
    #print('expected node:', expected,next_index,length)

    # #print('length,index',length,next_index)
    if isinstance(expected,np.str) and current_node['structure'] == expected:
        if next_index<length:
            current_node = node_list[next_index]
            next_index = next_index+1
        else:
            pass
        # #print('current_node:',current_node)
    elif isinstance(expected,np.int) and current_node['type'] == expected and next_index<length:
        # current_node = node_list[next_index]
        # next_index = next_index + 1
        if next_index<length:
            current_node = node_list[next_index]
            next_index = next_index+1
        else:
            pass
        # #print('current_node:',current_node)
    # elif isinstance(expected,dict) and next_index < length:
    #     current_node = node_list[next_index]
    #     next_index = next_index + 1
    elif isinstance(expected,dict):
        if(next_index < length):
            current_node = node_list[next_index]
        next_index = next_index+1

    else:
        raise(ValueError,'unexpected node!')

# 创建树节点
def new_node(node_type=config.NODE_TYPE['default']):
    node = {}
    if(node_type == config.NODE_TYPE['bracket']):
        node = {'structure':['(',{},')'],'type':config.NODE_TYPE['bracket']}
    elif node_type == config.NODE_TYPE['integer']:
        node = {'structure':0,'type':config.NODE_TYPE['integer']}
    elif node_type == config.NODE_TYPE['decimal']:
        node = {'structure':0,'type':config.NODE_TYPE['decimal']}
    elif node_type == config.NODE_TYPE['variable']:
        node = {'structure':'x','type':config.NODE_TYPE['variable'],'coefficient':1}
    elif node_type == config.NODE_TYPE['int']:
        node = {'structure':[],'type':node_type,'upper_bound':0,'lower_bound':0,'integral_var':0}
    elif node_type == config.NODE_TYPE['sqrt Main']:
        node = {'structure':[],'type':node_type,'times':2}
    # elif node_type == config.NODE_TYPE['t_pi']:
    #     node = {'structure':1,'type':node_type}
    elif node_type in [x[1] for x in config.NODE_TYPE.items()]:
        node = {'structure':[],'type':node_type}
    else:
        raise(ValueError,'new node:unknown node type')
    return node

def token_to_node(token):
    c = token['token_string']
    node = new_node()
    #print('token_to_node:', token)
    if c in config.SPECIAL or c in config.CMP:
        node = new_node(config.NODE_TYPE['default'])
        node['structure'] = c
    elif token['token_type']==config.TOKEN_TYPE['OPERATOR']:
        node = new_node(config.NODE_TYPE['operator'])
        node['structure'] = c
    elif token['token_type'] == config.TOKEN_TYPE['CONSTANT_INTEGER']:
        node = new_node(config.NODE_TYPE['integer'])
        node['structure'] = int(c)
        # match(config.TOKEN_TYPE['CONSTANT_INTEGER'])
    elif token['token_type'] == config.TOKEN_TYPE['CONSTANT_DECIMAL']:
        node = new_node(config.NODE_TYPE['decimal'])
        node['structure'] = float(c)
        # match(config.TOKEN_TYPE['CONSTANT_DECIMAL'])
    elif token['token_type'] == config.TOKEN_TYPE['VARIABLE']:
        node = new_node(config.NODE_TYPE['variable'])
        node['structure'] = c
        node['coefficient'] = token['coefficient']
        # match(config.TOKEN_TYPE['VARIABLE'])
    elif token['token_string'] in config.RESERVE or token['token_string'] in config.FUNCTION:
        # #print('wtf',config.TOKEN_TO_NODE[token['token_type']])
        node = new_node(config.TOKEN_TO_NODE[token['token_type']])
        node['structure'] = c
    # elif current_token['token_type'] == config.TOKEN_TYPE['']
