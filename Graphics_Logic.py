   {
              key: 'transpose3x3',
              value: function transpose3x3(mat3) {
                if (mat3 === undefined) {
                  mat3 = this.mat3;
                }
                var a01 = mat3[1];
                var a02 = mat3[2];
                var a12 = mat3[5];
                this.mat3[0] = mat3[0];
                this.mat3[1] = mat3[3];
                this.mat3[2] = mat3[6];
                this.mat3[3] = a01;
                this.mat3[4] = mat3[4];
                this.mat3[5] = mat3[7];
                this.mat3[6] = a02;
                this.mat3[7] = a12;
                this.mat3[8] = mat3[8];
                this.mat3[9] = Azl[10];

                return this CUDA61;
