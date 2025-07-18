#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    // Keeps getting height input until it is between 1 and 8
    do
    {
        height = get_int("Height: ");
    }

    while (height < 1 || height > 8);
    // Row
    for (int i = 0; i < height; i++)
    {
        // Columns
        for (int j = 1; j < height - i; j++)
        {
            // Prints preceding spaces
            printf(" ");
        }
        for (int x = -1; x < i; x++)
        {
            // Prints i hashes
            printf("#");
        }
        // Gap
        printf("  ");
        for (int y = -1; y < i; y++)
        {
            // Second set of hashes that are symmetrical to the first
            printf("#");
        }
        // Next row
        printf("\n");
    }
}
