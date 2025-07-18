#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    print_winner();
}

bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

void print_winner(void)
{
    candidate winners[candidate_count];

    for (int i = 0; i < candidate_count; i++)
    {
        // If candidate's vote count higher than current highest
        if (candidates[i].votes > winners[1].votes)
        {
            // Save candidate's vote count as first winner's vote count
            winners[1].votes = candidates[i].votes;
        }
    }

    for (int i = 0; i < candidate_count; i++)
    {
        // If candidate's vote count same as current highest
        if (candidates[i].votes == winners[1].votes)
        {
            // Add candidate to winners
            winners[i].name = candidates[i].name;
        }

        // If candidate's vote count not same as current highest
        else
        {
            winners[i].name = "";
        }
    }

    // Print names of winners
    for (int i = 0; i < candidate_count; i++)
    {
        if (winners[i].name[0] != '\0')
        {
            printf("%s\n", winners[i].name);
        }
    }

    return;
}
