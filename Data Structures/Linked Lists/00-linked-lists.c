Tek Yönlü Düğüm Yapısı
struct node {
  int data;               //Data
  struct node * nextNode  //Address
  };
    //Node isminde bir yapı tanımlanır, böyle bir yapıda istenilen türde istenildiği kadar eleman tanımlanabilir.
    //Şimdilik sadece tam sayı türünden tek bir eleman tanımlanmıştır.
    //nextNode, ismi ile bir pointer türünde bir yapı değişkeni tanımlanır. Sonraki düğümü işaret eder.

    //createNode() Function
struct linkedList * createNode(int data) {
  struct linkedList * newNode = 
    (struct linkedList*)malloc(sizeof(struct linkedList));
  newNode->data=data;
  newNode->nextNode=NULL
    return newNode;
}
    //bu fonksiyon, main() içerisinden her çağrıldığında bellekte, bağlı liste için düğüm oluşmasını sağlayacak 
    
    //Tek yönlü bağlı liste oluşturan ve listeye üç düğüm ekleyen C programı
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
struct linkedList{
  int data;
  struct linkedList *nextNode;
};
struct linkedList* firstNode=NULL
struct linkedList* createNode(int data) {
  struct linkedList* newNode =
    (struct linkedList*)malloc(sizeof(struct linkedList));
  newNode->data=data;
  newNode->nextNode=NULL;
  return newNode;
}
void printNode(){
  int n=0;
  struct linkedList

    








