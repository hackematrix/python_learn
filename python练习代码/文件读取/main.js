// 读取文件,写文件
import {readFile,writeFile} from 'node:fs/promises'

const data=await readFile('./pi_digits.txt','utf-8')

await writeFile('./progamming.txt','I love programming','utf-8')
    

console.log(data)
