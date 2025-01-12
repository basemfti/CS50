#include <stdio.h>
#include <stdlib.h>
#include<stdint.h>
#include<stdbool.h>

int main(int argc, char *argv[])
{
    if (argc!=2)
    {
        return 1;
    }
    FILE *raw_file=fopen(argv[1],"r");
    uint8_t buffer[512];
    bool found_jpg;
    int counter=0;
    char filename[8];
    FILE *img=NULL;
    while(fread(buffer,1,512,raw_file))
    {
        if (buffer[0]==0xff && buffer[1]==0xd8 && buffer[2]==0xff &&(buffer[3] & 0xf0)==0xe0)
        {
            found_jpg=true;

        }
        if (found_jpg==true)
        {
            if (counter!=0)
            {
                fclose(img);
            }


                sprintf(filename,"%03i.jpg",counter);
                img=fopen(filename,"w");
                fwrite(buffer,1,512,img);
                found_jpg=false;
                counter++;
        }

            else if (counter!=0)
            {
                fwrite(buffer,1,512,img);


            }




    }
    fclose(img);
    fclose(raw_file);


}
