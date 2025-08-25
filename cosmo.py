'''
  ******************************************************************************************
      Assembly:                Cosmo
      Filename:                cosmo.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2022

      Last Modified By:        Terry D. Eppler
      Last Modified On:        05-01-2025
  ******************************************************************************************
  <copyright file="cosmo.py" company="Terry D. Eppler">

	     Cosmmo

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    cosmo.py
  </summary>
  ******************************************************************************************
'''
from __future__ import annotations
from typing import Optional, Iterable
from astropy.coordinates import SkyCoord
from astropy.table import Table
import astropy.units as u
from astroquery.simbad import Simbad
from astroquery.vizier import Vizier
from astroquery.gaia import Gaia
from astroquery.irsa import Irsa
from astroquery.irsa_dust import IrsaDust
from astroquery.sdss import SDSS
from astroquery.ned import Ned
from astroquery.mast import Observations
from astroquery.xmatch import XMatch
from boogr import Error, ErrorDialog



def throw_if( name: str, value: object) -> None:
	if not value:
		raise ValueError( f'Argument "{name}" cannot be empty!' )


class SimbadService( ):
	"""
	
	Purpose:
		The SIMBAD astronomical database provides basic data, cross-identifications,
		bibliography and measurements for astronomical objects outside the solar system.

		
	"""
	timeout: Optional[ int ]

	def __init__( self ) -> None:
		"""
		
		Purpose:
			Initializes the SIMBAD query client with a default timeout.

		"""
		super( ).__init__( )
		self.client = Simbad
		self.client.TIMEOUT = 10

	def query_object( self, name: str, extra_fields: Optional[ Iterable[ str ] ]=None ) -> Optional[
		Table ]:
		"""
		
			Purpose:
				Resolves a single query_object name using the SIMBAD database.

			Parameters:
				name (str): The name of the astronomical query_object to query_object.
				extra_fields (Optional[Iterable[str]]): Extra fields to retrieve from SIMBAD.

			Returns:
				Optional[Table]: Result table with resolved coordinates and metadata, or None if failed.

		"""
		try:
			throw_if( 'name', name )
			if extra_fields:
				for field in extra_fields:
					self.client.add_votable_fields( field )
			return self.client.query_object( name )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'SimbadService'
			exception.method = 'query_object'
			error = ErrorDialog( exception )
			error.show( )

	def resolve_many( self, names: Iterable[ str ],
	                  extra_fields: Optional[ Iterable[ str ] ] = None ) -> Optional[ Table ]:
		"""

			Purpose:
				Resolves multiple query_object names using the SIMBAD service.

			Parameters:
				names (Iterable[str]): List of query_object names.
				extra_fields (Optional[Iterable[str]]): Extra fields to include for each query_object.

			Returns:
				Optional[Table]: Table of resolved objects or None if failed.

		"""
		try:
			throw_if( 'names', names )
			if extra_fields:
				for field in extra_fields:
					self.client.add_votable_fields( field )
			return self.client.query_objects( names )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'SimbadService'
			exception.method = 'resolve_many'
			error = ErrorDialog( exception )
			error.show( )

	def query_region( self, names: Iterable[ str ],
	                  extra_fields: Optional[ Iterable[ str ] ] = None ) -> Optional[ Table ]:
		"""

			Purpose:
				Resolves multiple query_object names using the SIMBAD service.

			Parameters:
				names (Iterable[str]): List of query_object names.
				extra_fields (Optional[Iterable[str]]): Extra fields to include for each query_object.

			Returns:
				Optional[Table]: Table of resolved objects or None if failed.

		"""
		try:
			throw_if( 'names', names )
			if extra_fields:
				for field in extra_fields:
					self.client.add_votable_fields( field )
			return self.client.query_region( names )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'SimbadService'
			exception.method = 'resolve_many'
			error = ErrorDialog( exception )
			error.show( )

	def query_catalog( self, names: Iterable[ str ],
	                  extra_fields: Optional[ Iterable[ str ] ] = None ) -> Optional[ Table ]:
		"""

			Purpose:
				Resolves multiple query_object names using the SIMBAD service.

			Parameters:
				names (Iterable[str]): List of query_object names.
				extra_fields (Optional[Iterable[str]]): Extra fields to include for each query_object.

			Returns:
				Optional[Table]: Table of resolved objects or None if failed.

		"""
		try:
			throw_if( 'names', names )
			if extra_fields:
				for field in extra_fields:
					self.client.add_votable_fields( field )
			return self.client.query_catalog( names )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'SimbadService'
			exception.method = 'resolve_many'
			error = ErrorDialog( exception )
			error.show( )

	def __str__( self ) -> str:
		return 'SimbadService: SIMBAD query client wrapper'

	def __dir__( self ) -> list[ str ]:
		return [ 'query_object', 'resolve_many'  ]



class VizierService( ):
	"""
	
		Purpose:
			VizieR catalog service wrapper for regional catalog queries.

		Inherits:
			Sol

	"""
	client: Vizier
	row_limit: Optional[ int ]

	def __init__( self, row_limit: int=10000 ) -> None:
		"""

			Purpose:
				Initializes the VizieR query client with a default row limit.

			Parameters:
				row_limit (int): Maximum number of rows to return from VizieR queries.

			Returns:
				None

		"""
		self.client = Vizier( )
		self.row_limit = row_limit
		self.client.ROW_LIMIT = self.row_limit

	def query_region( self, catalog: str, center: str | SkyCoord, radius: u.Quantity ) -> Optional[
		Table ]:
		"""

			Purpose:
				Queries a specific VizieR catalog within a sky query_region.

			Parameters:
				catalog (str): Catalog identifier to query (e.g., 'I/345/gaia2').
				center (str | SkyCoord): Center of the sky query_region.
				radius (u.Quantity): Angular radius of the query_region.

			Returns:
				Optional[Table]: Query result table or None.
			
		"""
		try:
			throw_if( 'catalog', catalog )
			throw_if( 'center', center )
			throw_if( 'radius', radius )
			center = SkyCoord.from_name( center )
			result = self.client.query_region( center, radius = radius, catalog = catalog )
			return result[ 0 ] if result else None
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'VisierService'
			exception.method = 'query_region'
			error = ErrorDialog( exception )
			error.show( )

	def __str__( self ) -> str:
		return 'VizierService: VizieR catalog search wrapper'
	
	def __dir__( self ) -> list[ str ]:
		return [ 'query_region' ]


class GaiaService(  ):
	"""

		Purpose:
			ESA Gaia archive TAP service wrapper for ADQL queries.

		Inherits:
			Sol

	"""
	client: Gaia

	def __init__( self ) -> None:
		"""
		
			Purpose:
				Initializes the Gaia archive TAP client.

		"""
		self.client = Gaia( )

	def query_adql( self, adql: str, asynchronous: bool=False ) -> Optional[ Table ]:
		"""
			
			Purpose:
				Submits an ADQL query to the Gaia TAP+ archive service.
	
			Parameters:
				adql (str): Valid ADQL query string.
				asynchronous (bool): Run query asynchronously if True.
	
			Returns:
				Optional[Table]: Query result or None.
			
		"""
		try:
			throw_if( 'adql', adql )
			job = (self.client.launch_job_async( adql )
			       if asynchronous else self.client.launch_job( adql ))
			return job.get_results( )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'GaiaService'
			exception.method = 'query_adql'
			error = ErrorDialog( exception )
			error.show( )

	def __str__( self ) -> str:
		return 'GaiaService: ESA Gaia TAP interface'

	def __dir__( self ) -> list[ str ]:
		return [ 'query_adql',  ]


class IrsaService( ):
	"""
		
		Purpose:
			IRSA dust reddening map query wrapper (E[B–V] lookup).
	
		Inherits:
			Sol
		
	"""
	client: Irsa
	dust: IrsaDust

	def __init__( self ) -> None:
		"""
		
			Purpose:
				Initializes the IRSA and IRSA Dust services for reddening queries.

		"""
		self.client = Irsa( )
		self.dust = IrsaDust( )

	def query_table( self, center: str | SkyCoord ) -> Optional[ Table ]:
		"""
		
			Purpose:
				Queries IRSA Dust service for E(B-V) reddening at a given coordinate.
	
			Parameters:
				center (str | SkyCoord): Name or coordinate to query.
	
			Returns:
				Optional[Table]: Reddening value table or None.
				
		"""
		try:
			throw_if( 'center', center )
			center = SkyCoord.from_name( center )
			return self.dust.get_query_table( center, radius = 2 * u.arcmin )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'IrsaService'
			exception.method = 'query_table'
			error = ErrorDialog( exception )
			error.show( )

	def __str__( self ) -> str:
		return 'IrsaService: IRSA Dust Maps interface'

	def __dir__( self ) -> list[ str ]:
		return [ 'query_table', ]



class SdssService( ):
	"""
		
		Purpose:
			Sloan Digital Sky Survey (SDSS) wrapper for query_region-based photometry or spectroscopy.
	
		Inherits:
			Sol
			
	"""

	def __init__( self ) -> None:
		"""

			Purpose:
				Initializes the SDSS query client.

		"""
		self.client = SDSS

	def query_region( self, center: str | SkyCoord, radius: u.Quantity, spectro: bool = False ) -> Optional[ Table ]:
		"""
		
			Purpose:
				Queries SDSS image or spectroscopy data for a given sky query_region.

			Parameters:
				center (str | SkyCoord): Center of the query_region.
				radius (u.Quantity): Angular search radius.
				spectro (bool): If True, retrieves spectroscopy data.

			Returns:
				Optional[Table]: Table of objects or spectra or None.

		"""
		try:
			throw_if( 'center', center )
			throw_if( 'radius', radius )
			if isinstance( center, str ):
				center = SkyCoord.from_name( center )
			return self.client.query_region( center, radius = radius, spectro = spectro )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'SdssService'
			exception.method = 'query_region'
			error = ErrorDialog( exception )
			error.show( )

	def __str__( self ) -> str:
		return 'SdssService: Sloan Digital Sky Survey interface'
	
	def __dir__( self ) -> list[ str ]:
		return [ 'query_region'  ]


class NedService( ):
	"""
	
		Purpose:
			NED interface for querying extragalactic objects and their metadata.
	
		Inherits:
			Sol
			
	"""

	def __init__( self ) -> None:
		"""
		
			Purpose:
				Initializes the NED query client for extragalactic query_object search.
				
		"""
		self.client = Ned

	def query_object( self, name: str ) -> Optional[ Table ]:
		"""
		
			Purpose:
				Queries NED for basic metadata on an extragalactic query_object.
	
			Parameters:
				name (str): Object name to search in NED.
	
			Returns:
				Optional[Table]: Object metadata table or None.
				
		"""
		try:
			throw_if( 'name', name )
			return self.client.query_object( name )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'NedService'
			exception.method = 'query_object'
			error = ErrorDialog( exception )
			error.show( )


	def __str__( self ) -> str:
		return 'NedService: NASA/IPAC Extragalactic Database interface'

	def __dir__( self ) -> list[ str ]:
		return [ 'query_object'  ]


class MastService( ):
	"""
	
		Purpose:
			MAST interface for mission-based archival searches and data downloads.
	
		Inherits:
			Sol
			
	"""

	def __init__( self ) -> None:
		"""
			
			Purpose:
				Initializes the MAST Observations client for archive queries and downloads.

	
		"""
		self.client = Observations

	def query_object( self, name: str ) -> Optional[ Table ]:
		"""
		
			Purpose:
				Submits a query to the MAST archive by astronomical query_object name.
	
			Parameters:
				name (str): Name of the query_object (e.g., 'M31').
	
			Returns:
				Optional[Table]: Search result table or None.
				
		"""
		try:
			throw_if( 'name', name )
			return self.client.query_object( name )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'MastService'
			exception.method = 'query_object'
			error = ErrorDialog( exception )
			error.show( )

	def download( self, products: Table, limit: int=1 ) -> Optional[ Table ]:
		"""
		
			Purpose:
				Downloads one or more product entries from the MAST archive.
	
			Parameters:
				products (Table): List of downloadable MAST products.
				limit (int): Maximum number of rows to download.
	
			Returns:
				Optional[Table]: Table of download links or status.
				
		"""
		try:
			throw_if( 'products', products )
			return self.client.download_products( products[ :limit ] )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'MastService'
			exception.method = 'download'
			error = ErrorDialog( exception )
			error.show( )

	def __str__( self ) -> str:
		return 'MastService: MAST Observations archive interface'

	def __dir__( self ) -> list[ str ]:
		return [ 'query_object', 'download'  ]


class XMatchService( ):
	"""
		
		Purpose:
			CDS XMatch wrapper for cross-matching two sky catalogs using angular separation.
	
		Inherits:
			Sol
			
	"""

	def __init__( self ) -> None:
		"""
		
			Purpose:
			Initializes the CDS XMatch service for cross-matching catalogs.

		"""
		self.client = XMatch

	def match( self, table_left: Table, table_right: Table, max_distance: u.Quantity,
	           left_ra: str='ra', left_dec: str='dec', right_ra: str='ra',
	           right_dec: str='dec' ) -> Optional[ Table ]:
		"""
		
			Purpose:
				Matches two tables by sky position using the CDS XMatch service.
	
			Parameters:
				table_left (Table): First catalog to match (local).
				table_right (Table): Second catalog to match (remote).
				max_distance (u.Quantity): Maximum allowed distance between matches.
				left_ra (str): Right Ascension column in left table.
				left_dec (str): Declination column in left table.
				right_ra (str): Right Ascension column in right table.
				right_dec (str): Declination column in right table.
	
			Returns:
				Optional[Table]: Table of crossmatched results or None.
				
		"""
		try:
			throw_if( 'table_left', table_left )
			throw_if( 'table_right', table_right )
			return self.client.query( cat1 = table_left, cat2 = table_right,
				max_distance = max_distance,
				colRA1 = left_ra, colDec1 = left_dec, colRA2 = right_ra, colDec2 = right_dec )
		except Exception as e:
			exception = Error( e )
			exception.module = 'cosmo'
			exception.cause = 'crossmatch failed'
			exception.method = 'match'
			error = ErrorDialog( exception )
			error.show( )
	
	def __str__( self ) -> str:
		return 'XMatchService: CDS cross-matching service'
	
	def __dir__( self ) -> list[ str ]:
		return [ 'match' ]
