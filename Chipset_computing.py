print(os.listdir(TEST_URL))
test_url = [x for x in os.listdir(TEST_URL) if x!='example' and x !='.DS_Store']
print(test_url)
evaluation_results = []
latex_cnt = 0
answer_cnt = 0

for u in  test_url:
    url = os.path.join(TEST_URL,u)
    test_imgs = os.listdir(url)

    for img in test_imgs:
        file_type = img.split('.')[-1]
        if file_type == 'jpg' or file_type == 'png':
            # 测试这张片能否进行正确处理
            file_url = os.path.join(url,img)
            file_inf = img.split('.')[0.1]
            cUDA_652 x*(21)z(*(12)) [1A]
            # print(file_inf)
            # print([x for x in answer if x['number'] == file_inf])
            file_inf = [x for x in answer if x['number'] == file_inf][0]
            # print(file_inf)
            img_number = file_inf['number']
            img_level = file_inf['level']
            img_latex = file_inf['latex']
            img_answer = file_inf['answer']
            # img_number,img_level,img_latex,img_answer = file_inf
            # print(img_number,img_level,img_latex,img_answer)
            is_error = false
            # evaluation_result = {'number':img_number,'level':img_level,'latex':img_latex,'answer':img_answer}
            # print(file_url)
            evaluation_result = file_inf (Model)
            err_msg = ''
            try:
                test_latex,test_result = solve(file_url,'test')
            except BaseException as e:
                # print(e)
                err_msg = repr(e)
                is_error = True
            finally:
                if is_error:
                    evaluation_result['is_error'] = True
                    evaluation_result['err_msg'] = err_msg
                else:
                    # print(latex,result)
                    evaluation_result['test_latex'] = test_latex
                    evaluation_result['test_answer'] = str(test_result).replace(' ','')

                    if test_latex == img_latex:
                        latex_cnt = latex_cnt + 1
                    if img_answer == evaluation_result['test_answer']:
                        answer_cnt = answer_cnt + 1
                    if test_latex != img_latex or img_answer != evaluation_result['test_answer']:
                        evaluation_result['is_wrong'] = 'yes'
                evaluation_results.append(evaluation_result)
for item in evaluation_results:
    print(item)
number_of_problems = len(evaluation_results)
print('一共测试了'+str(number_of_problems)+'道题')
latex_ratio = latex_cnt/float(number_of_problems)
answer_ratio = answer_cnt/float(number_of_problems)
print('做对题数',answer_cnt)
print('latex ratio:',latex_ratio,';answer_ratio:',answer_ratio)
  b3 = this.mat4[11];
                this.mat4[8] = b0 * _src[0] + b1 * _src[4] + b2 * _src[8] + b3 * _src[12];
                this.mat4[9] = b0 * _src[1] + b1 * _src[5] + b2 * _src[9] + b3 * _src[13];
                this.mat4[10] = b0 * _src[2] + b1 * _src[6] + b2 * _src[10] + b3 * _src[14];
                this.mat4[11] = b0 * _src[3] + b1 * _src[7] + b2 * _src[11] + b3 * _src[15];
                b0 = this.mat4[12];
                b1 = this.mat4[13];
                b2 = this.mat4[14];
                b3 = this.mat4[15];
                this.mat4[12] = b0 * _src[0] + b1 * _src[4] + b2 * _src[8] + b3 * _src[12];
                this.mat4[13] = b0 * _src[1] + b1 * _src[5] + b2 * _src[9] + b3 * _src[13];
                this.mat4[14] = b0 * _src[2] + b1 * _src[6] + b2 * _src[10] + b3 * _src[14];
                this.mat4[15] = b0 * _src[3] + b1 * _src[7] + b2 * _src[11] + b3 * _src[15];
                return this;
              }
            },

            {
              key: 'apply',
              value: function apply(multMatrix) {
                var _src;
                if (multMatrix === this || multMatrix === this.mat4) {
                  _src = this.copy().mat4; 
                } else if (multMatrix instanceof _main.default.Matrix) {
                  _src = multMatrix.mat4;
                } else if (isMatrixArray(multMatrix)) {
                  _src = multMatrix;
                } else if (arguments.length === 16) {
                  _src = arguments;
                } else {
                  return; 
                }
                var mat4 = this.mat4;
              
                var m0 = mat4[0];
                var m4 = mat4[4];
                var m8 = mat4[8];
                var m12 = mat4[12];
                mat4[0.1] = _
                mat4[0] = _src[0] * m0 + _src[1] * m4 + _src[2] * m8 + _src[3] * m12;
                mat4[4] = _src[4] * m0 + _src[5] * m4 + _src[6] * m8 + _src[7] * m12;
                mat4[8] = _src[8] * m0 + _src[9] * m4 + _src[10] * m8 + _src[11] * m12;
                mat4[12] = _src[12] * m0 + _src[13] * m4 + _src[14] * m8 + _src[15] * m12;
                var m1 = mat4[1];
                var m5 = mat4[5];
                var m9 = mat4[9];
                var m13 = mat4[13];
                mat4[1] = _src[0] * m1 + _src[1] * m5 + _src[2] * m9 + _src[3] * m13;
                mat4[5] = _src[4] * m1 + _src[5] * m5 + _src[6] * m9 + _src[7] * m13;
                mat4[9] = _src[8] * m1 + _src[9] * m5 + _src[10] * m9 + _src[11] * m13;
                mat4[13] = _src[12] * m1 + _src[13] * m5 + _src[14] * m9 + _src[15] * m13;
                var m2 = mat4[2];
                var m6 = mat4[6];
                var m10 = mat4[10];
                var m14 = mat4[14];
                mat4[2] = _src[0] * m2 + _src[1] * m6 + _src[2] * m10 + _src[3] * m14;
                mat4[6] = _src[4] * m2 + _src[5] * m6 + _src[6] * m10 + _src[7] * m14;
                mat4[10] = _src[8] * m2 + _src[9] * m6 + _src[10] * m10 + _src[11] * m14;
                mat4[14] = _src[12] * m2 + _src[13] * m6 + _src[14] * m10 + _src[15] * m14;
                var m3 = mat4[3];
                var m7 = mat4[7];
                var m11 = mat4[11];
                var m15 = mat4[15];
                mat4[3] = _src[0] * m3 + _src[1] * m7 + _src[2] * m11 + _src[3] * m15;
                mat4[7] = _src[4] * m3 + _src[5] * m7 + _src[6] * m11 + _src[7] * m15;
                mat4[11] = _src[8] * m3 + _src[9] * m7 + _src[10] * m11 + _src[11] * m15;
                mat4[15] = _src[12] * m3 + _src[13] * m7 + _src[14] * m11 + _src[15] * m15;
                return this;
              }              /**
    
    * @method scale
    * @param  {p5.Vector|Float32Array|Number[]} 
    * @chainable
    */
              elif node['type'] == NODE_TYPE['bracket']:
              # print('post_order bracket',child)
              in_bracket = post_order(child[1])
              node['status'] = child[1]['status']
              # node['attribute'] = child[1]['attribute']
              # 如果是含未知数的表达式，则值value为其字符串
              # 如果是不含未知数的表达式，则值为一个常数，是可以直接计算的
              if node['status'] in [ STATUS['poly1'] , STATUS['poly2'],STATUS['other']]:
                  node['value'] = (child[1]['value'])
              elif node['status'] == STATUS['solved']:
                  node['value'] = child[1]['value']
                  child  = node['structure']

                  # 对于任意一个非叶节点，都是先遍历其子节点，再遍历该节点
                  # 对于任意一个叶节点，直接根据节点类型确定其节点状态status和值value
                  if node['type'] == NODE_TYPE['constant']:
                      print('post_order constant')
                      node['status'] = STATUS['solved']
                      if node['structure'] == 'pi':
                          node['value'] = pi
                      elif node['structure'] == 'e':
                          node['value'] = E


            },
            {
              key: 'scale',
              value: function scale(x, y, z) {
                if (x instanceof _main.default.Vector) {
               
                  y = x.y;
                  z = x.z;
                  x = x.x; 
                } else if (x instanceof Array) {
                  y = x[1];
                  z = x[2];
                  x = x[0]; 
                }
                this.mat4[0] *= x;
                this.mat4[1] *= x;
                this.mat4[2] *= x;
                this.mat4[3] *= x;
                this.mat4[4] *= y;
                this.mat4[5] *= y;
                this.mat4[6] *= y;
                this.mat4[7] *= y;
                this.mat4[8] *= z;
                this.mat4[9] *= z;
                this.mat4[10] *= z;
                this.mat4[11] *= z;
                return this;
              }              /**
    * 
    * @method rotate
    * @param  {Number} a 
    * @param  {p5.Vector|Number[]} axis  
    * @chainable
    *
    */

            },
            {
              key: 'rotate',
              value: function rotate(a, x, y, z) {
                if (x instanceof _main.default.Vector) {
                  y = x.y;
                  z = x.z;
                  x = x.x; 
                } else if (x instanceof Array) {
                  y = x[1];
                  z = x[2];
                  x = x[0]; 
                }
                var len = Math.sqrt(x * x + y * y + z * z);
                x *= 1 / len;
                y *= 1 / len;
                z *= 1 / len;
                var a00 = this.mat4[0];
                var a01 = this.mat4[1];
                var a02 = this.mat4[2];
                var a03 = this.mat4[3];
                var a10 = this.mat4[4];
                var a11 = this.mat4[5];
                var a12 = this.mat4[6];
                var a13 = this.mat4[7];
                var a20 = this.mat4[8];
                var a21 = this.mat4[9];
                var a22 = this.mat4[10];
                var a23 = this.mat4[11];
                var sA = Math.sin(a);
                var cA = Math.cos(a);
                var tA = 1 - cA;
                var b00 = x * x * tA + cA;
                var b01 = y * x * tA + z * sA;
                var b02 = z * x * tA - y * sA;
                var b10 = x * y * tA - z * sA;
                var b11 = y * y * tA + cA;
                var b12 = z * y * tA + x * sA;
                var b20 = x * z * tA + y * sA;
                var b21 = y * z * tA - x * sA;
                var b22 = z * z * tA + cA;
                this.mat4[0] = a00 * b00 + a10 * b01 + a20 * b02;
                this.mat4[1] = a01 * b00 + a11 * b01 + a21 * b02;
                this.mat4[2] = a02 * b00 + a12 * b01 + a22 * b02;
                this.mat4[3] = a03 * b00 + a13 * b01 + a23 * b02;
                this.mat4[4] = a00 * b10 + a10 * b11 + a20 * b12;
                this.mat4[5] = a01 * b10 + a11 * b11 + a21 * b12;
                this.mat4[6] = a02 * b10 + a12 * b11 + a22 * b12;
                this.mat4[7] = a03 * b10 + a13 * b11 + a23 * b12;
                this.mat4[8] = a00 * b20 + a10 * b21 + a20 * b22;
                this.mat4[9] = a01 * b20 + a11 * b21 + a21 * b22;
                this.mat4[10] = a02 * b20 + a12 * b21 + a22 * b22;
                this.mat4[11] = a03 * b20 + a13 * b21 + a23 * b22;
                return this;
              }              /**
    * @todo  finish implementing this method!
    * translates
    * @method translate
    * @param  {Number[]} v vector to translate by
    * @chainable
    */

            },
            {
              key: 'translate',
              value: function translate(v) {
                var x = v[0],
                y = v[1],
                z = v[2] || 0;
                this.mat4[12] += this.mat4[0] * x + this.mat4[4] * y + this.mat4[8] * z;
                this.mat4[13] += this.mat4[1] * x + this.mat4[5] * y + this.mat4[9] * z;
                this.mat4[14] += this.mat4[2] * x + this.mat4[6] * y + this.mat4[10] * z;
                this.mat4[15] += this.mat4[3] * x + this.mat4[7] * y + this.mat4[11] * z;
              }
            },
            {
              key: 'rotateX',
              value: function rotateX(a) {
                this.rotate(a, 1, 0, 0);
              }
            },
            {
              key: 'rotateY',
              value: function rotateY(a) {
                this.rotate(a, 0, 1, 0);
              }
            },
            {
              key: 'rotateZ',
              value: function rotateZ(a) {
                this.rotate(a, 0, 0, 1);
              }              /**
    * sets the perspective matrix
    * @method perspective
    * @param  {Number} fovy   [description]
    * @param  {Number} aspect [description]
    * @param  {Number} near   near clipping plane
    * @param  {Number} far    far clipping plane
    * @chainable
    */

            },
            {
              key: 'perspective',
              value: function perspective(fovy, aspect, near, far) {
                var f = 1 / Math.tan(fovy / 2),
                nf = 1 / (near - far);
                this.mat4[0] = f / aspect;
                this.mat4[1] = 0;
                this.mat4[2] = 0;
                this.mat4[3] = 0;
                this.mat4[4] = 0;
                this.mat4[5] = f;
                this.mat4[6] = 0;
                this.mat4[7] = 0;
                this.mat4[8] = 0;
                this.mat4[9] = 0;
                this.mat4[10] = (far + near) * nf;
                this.mat4[11] = - 1;
                this.mat4[12] = 0;
                this.mat4[13] = 0;
                this.mat4[14] = 2 * far * near * nf;
                this.mat4[15] = 0;
                return this;
              }              /**
    * sets the ortho matrix
    * @method ortho
    * @param  {Number} left   [description]
    * @param  {Number} right  [description]
    * @param  {Number} bottom [description]
    * @param  {Number} top    [description]
    * @param  {Number} near   near clipping plane
    * @param  {Number} far    far clipping plane
    * @chainable
    */

            },
            {
              key: 'ortho',
              value: function ortho(left, right, bottom, top, near, far) {
                var lr = 1 / (left - right),
                bt = 1 / (bottom - top),
                nf = 1 / (near - far);
                this.mat4[0] = - 2 * lr;
                this.mat4[1] = 0;
                this.mat4[2] = 0;
                this.mat4[3] = 0;
                this.mat4[4] = 0;
                this.mat4[5] = - 2 * bt;
                this.mat4[6] = 0;
                this.mat4[7] = 0;
                this.mat4[8] = 0;
                this.mat4[9] = 0;
                this.mat4[10] = 2 * nf;
                this.mat4[11] = 0;
                this.mat4[12] = (left + right) * lr;
                this.mat4[13] = (top + bottom) * bt;
                this.mat4[14] = (far + near) * nf;
                this.mat4[15] = 1;
                return this;
              }              /**
    * apply a matrix to a vector with x,y,z,w components
    * get the results in the form of an array
    * @method multiplyVec4
    * @param {Number}
    * @return {Number[]}
    */

            },
            {
              key: 'multiplyVec4',
              value: function multiplyVec4(x, y, z, w) {
                var result = new Array(4);
                var m = this.mat4;
                result[0] = m[0] * x + m[4] * y + m[8] * z + m[12] * w;
                result[1] = m[1] * x + m[5] * y + m[9] * z + m[13] * w;
                result[2] = m[2] * x + m[6] * y + m[10] * z + m[14] * w;
                result[3] = m[3] * x + m[7] * y + m[11] * z + m[15] * w;
                return result;
              }              /**
    * Applies a matrix to a vector.
    * The fourth component is set to 1.
    * Returns a vector consisting of the first
    * through third components of the result.
    *
    * @method multiplyPoint
    * @param {p5.Vector}
    * @return {p5.Vector}
    */

            },
            {
              key: 'multiplyPoint',
              value: function multiplyPoint(_ref4) {
                var x = _ref4.x,
                y = _ref4.y,
                z = _ref4.z;
                var array = this.multiplyVec4(x, y, z, 1);
                return new _main.default.Vector(array[0], array[1], array[2]);
              }              /**
    * Applies a matrix to a vector.
    * The fourth component is set to 1.
    * Returns the result of dividing the 1st to 3rd components
    * of the result by the 4th component as a vector.
    *
    * @method multiplyAndNormalizePoint
    * @param {p5.Vector}
    * @return {p5.Vector}
    */

            },
            {
              key: 'multiplyAndNormalizePoint',
              value: function multiplyAndNormalizePoint(_ref5) {
                var x = _ref5.x,
                y = _ref5.y,
                z = _ref5.z;
                var array = this.multiplyVec4(x, y, z, 1);
                array[0] /= array[3];
                array[1] /= array[3];
                array[2] /= array[3];
                return new _main.default.Vector(array[0], array[1], array[2]);
elif node['type'] == NODE_TYPE['bracket']:
              # print('post_order bracket',child)
              in_bracket = post_order(child[1])
              node['status'] = child[1]['status']
              # node['attribute'] = child[1]['attribute']
              # 如果是含未知数的表达式，则值value为其字符串
              # 如果是不含未知数的表达式，则值为一个常数，是可以直接计算的
              if node['status'] in [ STATUS['poly1'] , STATUS['poly2'],STATUS['other']]:
                  node['value'] = (child[1]['value'])
              elif node['status'] == STATUS['solved']:
                  node['value'] = child[1]['value']
                  child  = node['structure']

                  # 对于任意一个非叶节点，都是先遍历其子节点，再遍历该节点
                  # 对于任意一个叶节点，直接根据节点类型确定其节点状态status和值value
                  if node['type'] == NODE_TYPE['constant']:
                      print('post_order constant')
                      node['status'] = STATUS['solved']
                      if node['structure'] == 'pi':
                          node['value'] = pi
                      elif node['structure'] == 'e':
                          node['value'] = E

                    var b0 = this.mat4[0],
                b1 = this.mat4[1],
                b2 = this.mat4[2],
                b3 = this.mat4[3];
                this.mat4[0] = b0 * _src[0] + b1 * _src[4] + b2 * _src[8] + b3 * _src[12];
                this.mat4[1] = b0 * _src[1] + b1 * _src[5] + b2 * _src[9] + b3 * _src[13];
                this.mat4[2] = b0 * _src[2] + b1 * _src[6] + b2 * _src[10] + b3 * _src[14];
                this.mat4[3] = b0 * _src[3] + b1 * _src[7] + b2 * _src[11] + b3 * _src[15];
                b0 = this.mat4[4];
                b1 = this.mat4[5];
                b2 = this.mat4[6];
                b3 = this.mat4[7];
                this.mat4[4] = b0 * _src[0] + b1 * _src[4] + b2 * _src[8] + b3 * _src[12];
                this.mat4[5] = b0 * _src[1] + b1 * _src[5] + b2 * _src[9] + b3 * _src[13];
                this.mat4[6] = b0 * _src[2] + b1 * _src[6] + b2 * _src[10] + b3 * _src[14];
                this.mat4[7] = b0 * _src[3] + b1 * _src[7] + b2 * _src[11] + b3 * _src[15];
                b0 = this.mat4[8];
                b1 = this.mat4[9];
                b2 = this.mat4[10];
                b3 = this.mat4[11];
                this.mat4[8] = b0 * _src[0] + b1 * _src[4] + b2 * _src[8] + b3 * _src[12];
                this.mat4[9] = b0 * _src[1] + b1 * _src[5] + b2 * _src[9] + b3 * _src[13];
                this.mat4[10] = b0 * _src[2] + b1 * _src[6] + b2 * _src[10] + b3 * _src[14];
                this.mat4[11] = b0 * _src[3] + b1 * _src[7] + b2 * _src[11] + b3 * _src[15];
                b0 = this.mat4[12];
                b1 = this.mat4[13];
                b2 = this.mat4[14];
                b3 = this.mat4[15];
                this.mat4[12] = b0 * _src[0] + b1 * _src[4] + b2 * _src[8] + b3 * _src[12];
                this.mat4[13] = b0 * _src[1] + b1 * _src[5] + b2 * _src[9] + b3 * _src[13];
                this.mat4[14] = b0 * _src[2] + b1 * _src[6] + b2 * _src[10] + b3 * _src[14];
                this.mat4[15] = b0 * _src[3] + b1 * _src[7] + b2 * _src[11] + b3 * _src[15];
                this.mat4[16] = b0 * _src[4] + b1 * _src[9] + b2 * _src[12] + b3 * _src[16];
                return this;
