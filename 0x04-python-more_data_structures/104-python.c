#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print basic info about a Python bytes object
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;

if (!PyBytes_Check(p))
{
printf("[.] bytes object info\n");
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
printf("[.] bytes object info\n");
printf("  size: %zd\n", size);
printf("  trying string: %s\n", PyBytes_AsString(p));
printf("  first %zd bytes: ", (size > 10) ? 10 : size);
for (i = 0; i < (size > 10 ? 10 : size); i++)
printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
printf("\n");
}
