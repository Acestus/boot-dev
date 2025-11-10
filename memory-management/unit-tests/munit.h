#ifndef MUNIT_H
#define MUNIT_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct {
    const char* name;
    void (*test)(void);
} MunitTest;

typedef struct {
    const char* prefix;
    MunitTest* tests;
} MunitSuite;

#define munit_case(TYPE, NAME, BODY) \
    void NAME(void) BODY

#define munit_test(NAME, FUNC) {NAME, FUNC}
#define munit_null_test {NULL, NULL}
#define munit_suite(NAME, TESTS) {NAME, TESTS}

#define munit_assert_double_equal(a, b, msg) \
    do { \
        double _a = (a), _b = (b); \
        if (fabs(_a - _b) > 1e-6) { \
            printf("FAIL: %s\n  Expected: %.6f\n  Actual: %.6f\n", msg, _b, _a); \
            exit(1); \
        } else { \
            printf("PASS: %s\n", msg); \
        } \
    } while(0)

int munit_suite_main(MunitSuite* suite, void* user_data, int argc, char* argv[]) {
    printf("Running test suite: %s\n", suite->prefix);
    int passed = 0, total = 0;
    
    for (MunitTest* test = suite->tests; test->name != NULL; test++) {
        printf("Running test: %s\n", test->name);
        total++;
        test->test();
        passed++;
    }
    
    printf("\nTest Results: %d/%d tests passed\n", passed, total);
    return (passed == total) ? 0 : 1;
}

// Define macros for RUN and SUBMIT (Boot.dev specific)
#define RUN 1
#define SUBMIT 1

#endif // MUNIT_H
