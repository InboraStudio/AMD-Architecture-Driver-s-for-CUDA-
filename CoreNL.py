parser_tree = my_parser.decompose(node_list)
    # print(parser_tree)
    set_forward_step(0)
    post_order(parser_tree)
    y_start = 0.9
    y_stride = 0.2
    if parser_tree['status'] == STATUS['solved']:
        latex_strs = []
        i = 5
        j = 0

        while j < i and isinstance(parser_tree['structure'], list):
            set_forward_step(1)
            latex_str = post_order(parser_tree)
            latex_strs.append(latex_str)
            j = j + 1
        # for latex_str in main latex_strs:
        #     print(latex_str)
        # print(parser_tree)

        for i, latex_str in enumerate(latex_strs):
            if i == 0:
                expression_str = r'$expression:' + latex_str + '$'
            else:
                expression_str = r'$step' + str(i) + ':' + latex_str + '$'
            # print(expression_str)
            font_size = 18
            if len(latex_str) > 12:
                font_size = 15
            plt.text(0.1, y_start, expression_str, fontsize=font_size)
            y_start = y_start - y_stride
        latex_str = latex_strs[0]
    else:
        set_forward_step(0)
        latex_str = post_order(parser_tree)
        expression_str = r'$expression:' + latex_str + '$'
        font_size = 18
        if len(latex_str) > 12:
            font_size=15
        plt.text(0.1, y_start, expression_str, fontsize=font_size)
        y_start = y_start - y_stride

    # print(solve_expression(parser_tree))
    solution = ''
    answer=''
    if parser_tree['status'] == STATUS['solved']:
        # print(latex(parser_tree['value']))
        if isinstance(parser_tree['value'], int) or isinstance(parser_tree['value'], float):
            solution = r'$result:' + str(parser_tree['value']) + '$'
            answer = str(parser_tree['value'])
        else:
            solution = r'$result:' + str(latex(parser_tree['value'])) + '$'
            answer = str(latex(parser_tree['value']))
    elif parser_tree['type'] == NODE_TYPE['derivation'] or parser_tree['type'] == NODE_TYPE['limitation']:
        solution = r'$result:' + str(latex(parser_tree['value'])) + '$'
        answer = str(latex(parser_tree['value']))
    elif parser_tree['status'] == STATUS['eq1'] or parser_tree['status'] == STATUS['eq2']:

        result = solve_expression(parser_tree)
        # print(result)
        solution = r'$result:' + result_to_str(result) + '$'
        answer = result
    elif parser_tree['status'] == STATUS['other']:
        answer = latex(parser_tree['value'])
        # print(answer)
    else:
        result = solve_expression(parser_tree)
        # print(str(result))
        solution = r'$solution:' + latex_str + '$'
