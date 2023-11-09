#include <GL/glut.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

GLfloat k = -100.0f;
GLfloat kstep = 1.0f;

GLfloat z = 0.0f;
GLfloat zstep = 0.5f;

GLfloat panX = 0.0f;
GLfloat panY = 0.0f;
GLfloat zoomFactor = 1.0f;
GLfloat zoomStep = 0.1f;

void drawObject() {
    glBegin(GL_TRIANGLES);
    glVertex2i(50, -50);
    glVertex2i(0, 50);
    glVertex2i(-50, -50);
    glEnd();
}

void drawOutline() {
    glBegin(GL_LINE_LOOP);
    glVertex2i(-100, 100);
    glVertex2i(100, 100);
    glVertex2i(100, -100);
    glVertex2i(-100, -100);
    glEnd();
}

void init() {
    glClearColor(1.0f, 1.0f, 1.0f, 0.0f);
}

void timerFunc(int value) {
    if (k > 100 || k < -300)
        kstep = -kstep;

    k += kstep;

    if (z > 150 || z < 0)
        zstep = -zstep;

    z += zstep;

    glutPostRedisplay();
    glutTimerFunc(10, timerFunc, 1);
}

void displayFunc() {
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);

    // Quadro meio/esquerda - Panning Horizontal
    glLoadIdentity();
    gluOrtho2D(-100.0f + panX, 100.0f + panX, -100.0f, 100.0f);
    glViewport(0, 300, 300, 300);
    glColor3f(1.0f, 0.0f, 0.0f);
    drawObject();

    // Quadro meio/direita - Panning Vertical
    glLoadIdentity();
    gluOrtho2D(-100.0f, 100.0f, -100.0f + panY, 100.0f + panY);
    glViewport(300, 300, 300, 300);
    glColor3f(0.0f, 1.0f, 0.0f);
    drawObject();

    // Quadro baixo - Zoom-in e Zoom-out
    glLoadIdentity();
    gluOrtho2D(-z * zoomFactor, z * zoomFactor, -z * zoomFactor, z * zoomFactor);
    glViewport(0, 0, 600, 300);
    glColor3f(0.0f, 0.0f, 1.0f);
    drawObject();

    // Desenhar os quadrados de contorno
    glLoadIdentity();
    gluOrtho2D(-200, 200, -200, 200);
    glViewport(0, 0, 600, 600);

    // GL_MODELVIEW utilizada para aplicar transformações geométricas às coordenadas dos objetos
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glColor3f(0.0f, 0.0f, 0.0f);
    glTranslatef(-100, -100, 0);
    drawOutline();

    glLoadIdentity();
    glTranslatef(100, -100, 0);
    drawOutline();

    glLoadIdentity();
    glTranslatef(-100, 100, 0);
    drawOutline();

    glLoadIdentity();
    glTranslatef(100, 100, 0);
    drawOutline();

    glLoadIdentity();

    glutSwapBuffers();
}

// Função para processar teclas especiais (para panning e zoom)
void specialKeys(int key, int x, int y) {
    switch (key) {
        case GLUT_KEY_LEFT:
            panX -= 10.0f;
            break;
        case GLUT_KEY_RIGHT:
            panX += 10.0f;
            break;
        case GLUT_KEY_UP:
            panY += 10.0f;
            break;
        case GLUT_KEY_DOWN:
            panY -= 10.0f;
            break;
        case GLUT_KEY_PAGE_UP:
            zoomFactor += zoomStep;
            break;
        case GLUT_KEY_PAGE_DOWN:
            zoomFactor -= zoomStep;
            break;
    }

    glutPostRedisplay();
}

int main(int argc, char *argv[]) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowPosition(50, 50);
    glutInitWindowSize(600, 600);
    glutCreateWindow("Viewing 2D");
    glutDisplayFunc(displayFunc);
    glutSpecialFunc(specialKeys);  // Registra a função para processar teclas especiais
    glutTimerFunc(10, timerFunc, 1);
    init();
    glutMainLoop();
    return 0;
}
