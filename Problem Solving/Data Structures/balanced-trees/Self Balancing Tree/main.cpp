/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */


int heightt(struct node* a){
    if(a==NULL){
        return -1;
    }
    return a->ht;
}
int max(int a,int b){
    if(a>=b){
        return a;
    }
    return b;
}
struct node* newnode(int a){
    struct node* r=new node();
    r->val=a;
    r->left=NULL;
    r->right=NULL;
    r->ht=0;
    return r;
}
struct node* rightbal(struct node* x){
    struct node* y=x->left;
    struct node* t2=y->right;
    y->right=x;
    x->left=t2;
    x->ht= max(heightt(x->left),heightt(x->right))+1;
    y->ht= max(heightt(y->left),heightt(y->right))+1;
    return y;
}
struct node* leftbal(struct node* x){
    struct node* y=x->right;
    struct node* t2=y->left;
    y->left=x;
    x->right=t2;
    x->ht=max(heightt(x->left),heightt(x->right))+1;
    y->ht=max(heightt(y->right),heightt(y->left))+1;
    return y;
}
int balance(struct node* a){
    if(a==NULL){
        return -1;
    }
    return heightt(a->left) - heightt(a->right);
}
struct node* insert(struct node* root,int value)
{
    if(root==NULL){
        return newnode(value);
    }
    if(root->val>value){
        root->left=insert(root->left,value);
    }
    else if(root->val<value){
        root->right=insert(root->right,value);
    }
    root->ht=max(heightt(root->left),heightt(root->right))+1;
    int bf=balance(root);
    if(bf>1 && value < root->left->val){
        return rightbal(root);
    }
    if(bf<-1 && value > root->right->val){
        return leftbal(root);
    }
    if(bf>1 && value > root->left->val){
        root->left = leftbal(root->left);
        return rightbal(root);
    }
    if(bf<-1 && value < root->right->val){
        root->right=rightbal(root->right);
        return leftbal(root);
    }
    return root;
}
