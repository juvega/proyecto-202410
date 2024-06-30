import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SigetraLoginComponent } from './sigetra-login.component';

describe('SigetraLoginComponent', () => {
  let component: SigetraLoginComponent;
  let fixture: ComponentFixture<SigetraLoginComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SigetraLoginComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SigetraLoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
