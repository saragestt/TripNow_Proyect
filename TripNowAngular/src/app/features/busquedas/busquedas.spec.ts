import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Busquedas } from './busquedas';

describe('Busquedas', () => {
  let component: Busquedas;
  let fixture: ComponentFixture<Busquedas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Busquedas]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Busquedas);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
