# -*- coding: utf-8 -*-
"""
"""
import copy
import unittest
import numpy as np
if __name__ == '__main__':
    import sys
    sys.path.append("..")
    
    
    def filter_path(path_list, rem_nan = True, rem_overlap = True):
        """Filter illegal points on the path
        
        I
        """
    def resample_path(path):
        vert_start = path[0]
        #生成新路径点集
        new_path = [vert_start]
        vert_midle = path[1]
        for i in range(2, len(path)):
            vert_end = path[i]
                #生成向量
            v1 = vert_start - vert_midle
            v2 = vert_end - vert_midle
            angle = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
            #判断是否在一条直线上
            if(round(angle,1)!=1.0 and round(angle,1)!=-1.0):
                new_path.append(vert_midle)
                vert_start = vert_midle
                vert_midle = vert_end
            else:
                vert_midle=vert_end

        new_path.append(path[-1])

        return new_path  




class TestClass(unittest.TestCase):
    
    def test1(self):
        print("test1")
        
            
    def test2(self):
        print('test2')
        
    def test_resample(self):
        # 生成一组点，输入模拟路径
        path=np.loadtxt("C:/Users/LU/Desktop/robot3dprinter/suCAM-master/python/tools/CFPrinting/syc_cube_sample1(1).2.path")     
        new_path = np.asarray(resample_path(path))
        np.savetxt('C:/Users/LU/Desktop/syc_cube_sample1(1).2', new_path)
                
        print(new_path)

if __name__ == '__main__':
    unittest.main()