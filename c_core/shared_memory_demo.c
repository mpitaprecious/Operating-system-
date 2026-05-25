#include <stdio.h>
#include <windows.h>

int main() {

    HANDLE hMapFile;

    LPCTSTR message =
        "Hello from shared memory";

    LPVOID pBuf;

    hMapFile = CreateFileMapping(
        INVALID_HANDLE_VALUE,
        NULL,
        PAGE_READWRITE,
        0,
        256,
        "EduOSSharedMemory"
    );

    if (hMapFile == NULL) {

        printf("Could not create file mapping\n");

        return 1;
    }

    pBuf = MapViewOfFile(
        hMapFile,
        FILE_MAP_ALL_ACCESS,
        0,
        0,
        256
    );

    if (pBuf == NULL) {

        printf("Could not map view of file\n");

        CloseHandle(hMapFile);

        return 1;
    }

    CopyMemory(
        (PVOID)pBuf,
        message,
        strlen(message) + 1
    );

    printf(
        "Shared Memory Contains: %s\n",
        (char*)pBuf
    );

    UnmapViewOfFile(pBuf);

    CloseHandle(hMapFile);

    return 0;
}