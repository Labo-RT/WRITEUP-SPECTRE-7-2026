#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
#include <time.h>

void win() {
    printf("\n🎉 ADMIN ACCESS GRANTED! 🎉\n");
    system("cat flag.txt");
}

int digits(int n) {
    long x = n;
    if (x == 0) return 1;
    if (x < 0) x = -x;

    int count = 0;
    while (x) {
        x /= 10;
        count++;
    }
    return count;
}

void joke_generator() {
    char jokes[][100] = {
        "Why did the programmer quit their job? They didn't get arrays!",
        "What do you call a fake noodle? An impasta!",
        "Why do Java developers wear glasses? Because they can't C#!",
        "I would tell you a UDP joke, but you might not get it.",
        "Why do C programmers die young? They have no class!"
    };
    int index = rand() % 5;
    printf("\nJoke: %s\n", jokes[index]);
}

void view_profile(unsigned int tokens) {
    printf("\nYour Profile:\n");
    printf("  - User Level: Guest\n");
    printf("  - Tokens: %u\n", tokens);
    //printf("  - Jokes Told: 42\n");
    printf("  - Admin Status: DENIED\n");
}

void admin_panel() {
    int signed_input;
    unsigned int tokens;
    char buf[32];
    
    printf("\n--- ADMIN PANEL ---\n");
    printf("Requirement: at least 3.000.000.000 tokens\n");
    printf("\nYou have two options:\n");
    printf("1. Generate tokens one at a time\n");
    printf("2. Enter your current token count\n");
    printf("\nEnter your token count: ");
    
    if (scanf("%31s", buf) != 1) {
        printf("Invalid input!\n");
        return;
    }

    long long tmp = atoll(buf);

    if (tmp > INT_MAX || tmp < INT_MIN) {
        printf("Number out of range!\n");
        return;
    }

    signed_input = (int)tmp; 
    if (signed_input > 0 && digits(signed_input) >= 5) {
        printf("\n[SYSTEM] Manual entry detected: %d tokens\n", signed_input);
        printf("Liar! Nobody has that many tokens!\n");
        return;
    }
    
    tokens = (unsigned int)signed_input;
    
    if (signed_input < 0 && tokens > 3000000000) {
        printf("\n[NICE] Negative input detected!\n");
        printf("When converted to unsigned: %u tokens\n", tokens);
        printf("\nWow, you have %u tokens!\n", tokens);
        win();
    } else {
        printf("\nYou have %u tokens. Not enough for admin.\n", tokens);
    }
}

void generate_token(unsigned int *current_tokens) {
    (*current_tokens)++;
    printf("\n+1 token generated!\n");
    printf("Total tokens: %u\n", *current_tokens);
    printf("You need %u more tokens for admin access.\n", 
           (unsigned int)(3000000000U - *current_tokens));
}

void exit_menu() {
    printf("\nGoodbye!\n");
    exit(0);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    srand(time(NULL));
    
    unsigned int user_tokens = 0;
    int choice;
    
    printf("==================================================\n");
    printf("      WELCOME TO THE TOKEN TERMINAL\n");
    printf("==================================================\n");
    
    while (1) {
        printf("\n--- MENU ---\n");
        printf("1. Generate 1 token\n");
        printf("2. Tell me a joke\n");
        printf("3. View your profile\n");
        printf("4. Access admin panel\n");
        printf("5. Exit\n");
        printf("Choose (1-5): ");
        
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input!\n");
            while(getchar() != '\n');
            continue;
        }
        
        switch(choice) {
            case 1:
                generate_token(&user_tokens);
                break;
            case 2:
                joke_generator();
                break;
            case 3:
                view_profile(user_tokens);
                break;
            case 4:
                admin_panel();
                break;
            case 5:
                exit_menu();
                break;
            default:
                printf("\nInvalid choice!\n");
        }
    }
    
    return 0;
}
