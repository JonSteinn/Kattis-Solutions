#include <string.h>
#include <stdio.h>

int check(char* pw, size_t pw_len, char* str, size_t str_len)
{
    int str_current = 0, pw_current = 0, ret_val = -1;
    while(ret_val < 0)
    {
        if (str_current == str_len)
        {
            ret_val = 0;
        }
        else if (str[str_current] == pw[pw_current])
        {
            pw_current++;
            if (pw_current == pw_len)
            {
                ret_val = 1;
            }
        }
        else
        {
            for (int i = pw_current + 1; i < pw_len; i++)
            {
                if (pw[i] == str[str_current])
                {
                    ret_val = 0;
                    break;
                }
            }
        }
        str_current++;
    }
    return ret_val;
}

int main()
{
    char pw[9], str[41];
    scanf("%s %s",pw,str);
    printf(check(pw,strlen(pw),str,strlen(str)) ? "PASS\n" : "FAIL\n");
    return 0;
}