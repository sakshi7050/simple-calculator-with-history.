

#include <stdio.h>
#include <stdlib.h>

typedef struct History {
    float num1, num2, result;
    char operator;
    struct History* next;
} History;

History* head = NULL;

// Add operation to history
void add_to_history(float n1, float n2, char op, float res) {
    History* new_entry = (History*)malloc(sizeof(History));
    new_entry->num1 = n1;
    new_entry->num2 = n2;
    new_entry->operator = op;
    new_entry->result = res;
    new_entry->next = head;
    head = new_entry;
}

// Show all history
void show_history() {
    History* current = head;
    printf("\n--- Calculation History ---\n");
    while (current != NULL) {
        printf("%.2f %c %.2f = %.2f\n", current->num1, current->operator, current->num2, current->result);
        current = current->next;
    }
    printf("---------------------------\n");
}

int main() {
    float num1, num2, result;
    char operator;
    char choice;

    do {
        printf("Enter first number: ");
        scanf("%f", &num1);
        printf("Enter operator (+ - * /): ");
        scanf(" %c", &operator);
        printf("Enter second number: ");
        scanf("%f", &num2);

        switch (operator) {
            case '+': result = num1 + num2; break;
            case '-': result = num1 - num2; break;
            case '*': result = num1 * num2; break;
            case '/': 
                if (num2 != 0) result = num1 / num2;
                else {
                    printf("Error: Division by zero!\n");
                    continue;
                }
                break;
            default:
                printf("Invalid operator!\n");
                continue;
        }

        printf("Result: %.2f\n", result);
        add_to_history(num1, num2, operator, result);

        printf("Do you want to continue (y/n)? ");
        scanf(" %c", &choice);

    } while (choice == 'y' || choice == 'Y');

    show_history();
    return 0;
}

