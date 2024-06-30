import { Component, OnInit } from '@angular/core';

import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { ProductService } from './products.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {
  products: any[] = [];
  selectedProduct: any = {};
  closeResult = '';

  constructor(private productoService: ProductService, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.obtenerProductos();
  }

  obtenerProductos(): void {
    this.productoService.getProductos().subscribe((data: any[]) => {
      this.products = data;
    });
  }

  openCreateModal(content: any): void {
    this.selectedProduct = {}; // Reset selectedProduct for creation
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title' }).result.then(
      (result) => {
        this.closeResult = `Closed with: ${result}`;
      },
      (reason) => {
        this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
      }
    );
  }

  openEditModal(content: any, product: any): void {
    this.selectedProduct = { ...product };
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title' }).result.then(
      (result) => {
        this.closeResult = `Closed with: ${result}`;
      },
      (reason) => {
        this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
      }
    );
  }

  openConfirmModal(content: any, product: any): void {
    this.selectedProduct = { ...product };
    this.modalService.open(content, { ariaLabelledBy: 'modal-basic-title' }).result.then(
      (result) => {
        this.closeResult = `Closed with: ${result}`;
      },
      (reason) => {
        this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
      }
    );
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }

  guardarNuevoProducto(): void {
    this.productoService.createProducto(this.selectedProduct).subscribe(() => {
      this.obtenerProductos();
      this.modalService.dismissAll(); // Close the modal after saving
    });
  }

  guardarCambios(): void {
    this.productoService.updateProducto(this.selectedProduct.id, this.selectedProduct).subscribe(() => {
      this.obtenerProductos();
      this.modalService.dismissAll(); // Close the modal after saving
    });
  }

  confirmarEliminacion(): void {
    this.productoService.deleteProducto(this.selectedProduct.id).subscribe(() => {
      this.obtenerProductos(); // Refresh the list after deletion
      this.modalService.dismissAll(); // Close the modal after deletion
    });
  }

  

  eliminarProducto(id: number): void {
    this.productoService.deleteProducto(id).subscribe(() => {
      this.obtenerProductos(); // Refresh the list after deletion
    });
  }
}
