import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SigetraMenuComponent } from './sigetra-menu.component';

describe('SigetraMenuComponent', () => {
  let component: SigetraMenuComponent;
  let fixture: ComponentFixture<SigetraMenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SigetraMenuComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SigetraMenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
