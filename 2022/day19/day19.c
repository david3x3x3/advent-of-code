struct step_s {
  int inv[4];
  int robots[4];
}

int costs[][] = {
  {
    { { 4, 0, 0, 0}, { 2, 0, 0, 0 }, { 3, 14, 0, 0 }, { 2, 7, 0, 0 } },
    { { 2, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 8, 0, 0 }, { 3, 12, 0, 0 } },
  },
  {
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 17, 0, 0 }, { 4, 16, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 20, 0, 0 }, { 2, 8, 0, 0 } },
    { { 2, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 13, 0, 0 }, { 3, 15, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 2, 14, 0, 0 }, { 3, 17, 0, 0 } },
    { { 3, 0, 0, 0}, { 3, 0, 0, 0 }, { 2, 19, 0, 0 }, { 2, 20, 0, 0 } },
    { { 4, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 17, 0, 0 }, { 3, 13, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 7, 0, 0 }, { 2, 19, 0, 0 } },
    { { 3, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 19, 0, 0 }, { 2, 9, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 15, 0, 0 }, { 4, 17, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 2, 17, 0, 0 }, { 3, 11, 0, 0 } },
    { { 2, 0, 0, 0}, { 2, 0, 0, 0 }, { 2, 7, 0, 0 }, { 2, 14, 0, 0 } },
    { { 4, 0, 0, 0}, { 3, 0, 0, 0 }, { 2, 13, 0, 0 }, { 2, 10, 0, 0 } },
    { { 2, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 11, 0, 0 }, { 2, 16, 0, 0 } },
    { { 4, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 10, 0, 0 }, { 3, 10, 0, 0 } },
    { { 2, 0, 0, 0}, { 4, 0, 0, 0 }, { 3, 20, 0, 0 }, { 2, 16, 0, 0 } },
    { { 3, 0, 0, 0}, { 4, 0, 0, 0 }, { 3, 10, 0, 0 }, { 4, 8, 0, 0 } },
    { { 4, 0, 0, 0}, { 3, 0, 0, 0 }, { 2, 13, 0, 0 }, { 2, 9, 0, 0 } },
    { { 2, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 15, 0, 0 }, { 2, 20, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 2, 9, 0, 0 }, { 3, 19, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 2, 11, 0, 0 }, { 2, 7, 0, 0 } },
    { { 3, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 20, 0, 0 }, { 2, 12, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 2, 11, 0, 0 }, { 4, 8, 0, 0 } },
    { { 2, 0, 0, 0}, { 4, 0, 0, 0 }, { 3, 17, 0, 0 }, { 4, 20, 0, 0 } },
    { { 3, 0, 0, 0}, { 3, 0, 0, 0 }, { 3, 15, 0, 0 }, { 2, 8, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 5, 0, 0 }, { 3, 7, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 2, 8, 0, 0 }, { 3, 9, 0, 0 } },
    { { 3, 0, 0, 0}, { 4, 0, 0, 0 }, { 3, 19, 0, 0 }, { 3, 8, 0, 0 } },
    { { 4, 0, 0, 0}, { 4, 0, 0, 0 }, { 3, 7, 0, 0 }, { 4, 20, 0, 0 } },
    { { 3, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 20, 0, 0 }, { 4, 16, 0, 0 } },
    { { 2, 0, 0, 0}, { 4, 0, 0, 0 }, { 4, 13, 0, 0 }, { 3, 11, 0, 0 } },
  }
};

int
main(int argc, char *argv[]) {
}
