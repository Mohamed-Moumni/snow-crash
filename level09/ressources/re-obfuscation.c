#include <stdio.h>
#include <stdlib.h>


int hexToInt(const char *hexStr) {
    int decimalValue = 0;  // Resulting decimal value

    while (*hexStr) {
        decimalValue *= 16;  // Shift the current value by one hex digit

        // Convert the current character to its decimal value
        if (*hexStr >= '0' && *hexStr <= '9') {
            decimalValue += *hexStr - '0';  // Convert '0'-'9' to 0-9
        } else if (*hexStr >= 'a' && *hexStr <= 'f') {
            decimalValue += *hexStr - 'a' + 10;  // Convert 'a'-'f' to 10-15
        } else if (*hexStr >= 'A' && *hexStr <= 'F') {
            decimalValue += *hexStr - 'A' + 10;  // Convert 'A'-'F' to 10-15
        } else {
            // Invalid character in the hex string
            return -1;  // Return -1 to indicate error (you can handle this differently)
        }

        hexStr++;  // Move to the next character
    }

    return decimalValue;
}

int main(int argc, char **argv)
{
    int i = 1;
    char c = 0;
    while (argv[i] != NULL) {
        c = hexToInt(argv[i]);
        c -= i - 1;
        // printf("argv: %s\n", argv[i]);
        printf("%c", c);
        i++;
    }
    printf("\n");
    return 0;
}
