import EncryptTechnique as ET
import MultiEncryption as ME

def main():
    str = ET.getText('assign4text.txt')
    print(ET.countLetters(str))
    
    encrypt = ME.Encrypt(str, "01")
    print(ET.countLetters(encrypt))

if __name__=="__main__":
    main()