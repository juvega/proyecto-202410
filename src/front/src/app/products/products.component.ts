import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { ProductsService } from './products.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {
  products: any[] = [];
  selectedProduct: any = {};

  constructor(private productoService: ProductsService, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.getAllProducts();
  }

  getAllProducts(): void {
    this.productoService.getProductos().subscribe((data: any[]) => {
      
      this.products = data;
    });
  }

  openEditModal(product: any): void {
    this.selectedProduct = { ...product };
    const modal = document.getElementById('editProductModal');
    if (modal) {
      const bootstrapModal = new bootstrap.Modal(modal);
      bootstrapModal.show();
    }
  }

  guardarCambios(): void {
    this.productoService.updateProducto(this.selectedProduct.id, this.selectedProduct).subscribe(() => {
      this.getAllProducts();
      const modal = document.getElementById('editProductModal');
      if (modal) {
        const bootstrapModal = bootstrap.Modal.getInstance(modal);
        bootstrapModal.hide();
      }
    });
  }
  eliminarProducto(id: number): void {
    // Lógica para eliminar el producto
    this.productoService.deleteProducto(id).subscribe(() => {
      this.getAllProducts(); // Refrescar la lista después de eliminar
    });
  }
}
